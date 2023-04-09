import random
import os
import json
import signal
import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta

import structlog

log = structlog.get_logger()

CODE_LENGTH = 6
CODE_FILENAME = "code"
REQUEST_FILENAME = "request"
EXPIRATION = timedelta(seconds=30)

go = asyncio.create_task

def generate_code() -> str:
    code = ""
    for i in range(CODE_LENGTH):
        num = random.randint(0, 9)
        code = f"{code}{num}"
    return code


@dataclass
class Code:
    code: str
    timestamp: datetime
    user_id: int = 1
    used: bool = False


class Database:
    def __init__(self):
        self._data = []

    async def insert(self, code: Code):
        self._data.append(code)

    async def find(self, otp_code: str, user_id: int = 1):
        for item in self._data:
            if item.code == otp_code and item.user_id == user_id:
                return item


async def update_code(db: Database):
    try:
        while True:
            code = generate_code()
            new_code = Code(
                code=code,
                timestamp=datetime.now(),
            )
            await db.insert(new_code)
            with open(CODE_FILENAME, "w") as f:
                f.write(code)

            log.debug(f"Added new code {new_code}")
            await asyncio.sleep(60)
    except asyncio.CancelledError:
        log.warn("Server has been stopped")


async def check_access(db: Database):
    with open(REQUEST_FILENAME) as f:
        data = json.loads(f.read())
        otp_code = data.get("code")
        user_id = data.get("user_id")

    res : Code = await db.find(otp_code=otp_code, user_id=user_id)
    if res is None:
        log.error("Wrong user or OTP code!")
        return

    if datetime.now() - res.timestamp > EXPIRATION:
        log.warn("OTP code has expired!")
        return

    if res.user_id != user_id:
        log.error("Access denied!")
    else:
        log.warn("Access granted!")
        # TODO: set code as used



async def main():
    db = Database()

    update_task = go(update_code(db))

    try:
        loop = asyncio.get_event_loop()
        loop.add_signal_handler(signal.SIGUSR1, lambda: go(check_access(db)))
        log.info(f"Server is started on PID {os.getpid()}...")
        await update_task
    except KeyboardInterrupt:
        for task in asyncio.all_tasks():
            task.cancel()


if __name__ == "__main__":
    asyncio.run(main())