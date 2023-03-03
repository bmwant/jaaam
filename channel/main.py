import asyncio
from typing import Any


class Value:
    def __init__(self, value: Any = None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)


class Channel:
    def __init__(self, size: int = 0):
        self.size = size
        self._channel = asyncio.Queue(maxsize=size)

    async def __lshift__(self, value):
        print(f"Receiving {value}")
        return self._channel.put(value)

    async def __rshift__(self, value: Value):
        print(f"Sending {value}")
        new_value = await self._channel.get()
        value.value = new_value


async def main():
    c = Channel(size=5)
    v = Value(0)
    print(f"Initial value: {v}")
    await (c << 2)
    await (c >> v)
    # breakpoint()
    print(c._channel.qsize())
    print(f"Value received from a channel: {v}")


if __name__ == "__main__":
    asyncio.run(main())    
