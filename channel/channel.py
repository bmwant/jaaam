import asyncio
import logging
from typing import Any


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y/%m/%d %H:%M:%S")

class Value:
    def __init__(self, value: Any = None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

    async def __lshift__(self, channel: "Channel"):
        new_value = await channel.get()
        self.value = new_value


class Channel:
    def __init__(self, size: int = 0):
        self.size = size
        self._queue = asyncio.Queue(maxsize=size)
        self._closed = False

    async def __lshift__(self, value):
        logging.debug(f"Channel receiving {value}")
        return await self._queue.put(value)

    async def get(self):
        while True:
            if self.closed and self._queue.empty():
                return

            try:
                value = self._queue.get_nowait()
                return value
            except asyncio.QueueEmpty:
                await asyncio.sleep(0.1)

    async def __rshift__(self, value: Value):
        logging.debug(f"Channel sending {value}")
        new_value = await self.get()
        value.value = new_value

    def close(self):
        if self.closed:
            raise RuntimeError("panic: close of closed channel")
        self._closed = True

    @property
    def closed(self) -> bool:
        return self._closed


class Range:
    def __init__(self, channel: Channel):
        self._channel = channel

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self._channel.get()
        if value is None:
            raise StopAsyncIteration()
        return value


def Close(channel: Channel):
    channel.close()


go = asyncio.create_task


async def main():
    ch = Channel(size=2)
    exit = Channel()
    _ = Value()

    async def producer():
        for i in range(5):
            logging.info(f"Sending {i}")
            await (ch << i)
            logging.info(f"Sent {i}")
            await asyncio.sleep(1)

        logging.info("Finished producing")
        Close(ch)

    async def consumer():
        async for i in Range(ch):
            logging.info(f"Received {i}")

        # await asyncio.sleep(2)
        logging.info("Finished consuming")
        Close(exit)

    go(producer())
    go(consumer())

    logging.info("Waiting for everything to complete")
    await (_ << exit)
    logging.info("All done, exiting!")


async def test():
    ch = Channel()
    v = Value()

    # Sending values to a channel
    await (ch << 23)
    await (ch << "this is a string")

    # Receiving values from channel
    await (v << ch)
    print(f"v holds '{v}' value")
    await (v << ch)
    print(f"v now holds '{v}' value")


if __name__ == "__main__":
    # asyncio.run(test())
    asyncio.run(main())
