import asyncio
from dataclasses import dataclass
from enum import IntEnum, StrEnum, auto


class AgendID(IntEnum):
    SHOP = auto()
    CLIENT = auto()


@dataclass
class Message:
    agent_id: str
    text: float


class MessagePump(asyncio.Queue):
    async def peek(self):
        if not self.empty():
            return self._queue[0]
