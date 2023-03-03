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
        self._closed = False

    async def __lshift__(self, value):
        # print(f"Receiving {value}")
        return await self._channel.put(value)

    async def get(self):
        while True:
            if self.closed:
                return

            try:
                value = self._channel.get_nowait()
                return value
            except asyncio.QueueEmpty:
                await asyncio.sleep(0.1)

    async def __rshift__(self, value: Value):
        # print(f"Sending {value}")
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
        if self._channel.closed:
            raise StopAsyncIteration()
        return await self._channel.get()


def Close(channel: Channel):
    channel.close()


go = asyncio.create_task


async def main():
    ch = Channel(size=5)
    exit = Channel()
    _ = Value()

    async def producer():
        for i in range(5):
            print(f"Sending {i}")
            await (c << i)
            print(f"Sent {i}")

        print("Finished producing")
        Close(ch)

    async def consumer():
        async for i in Range(ch):
            print(f"Received {i}")
        
        await asyncio.sleep(2)
        print("Finished consuming")
        Close(exit)

    go(producer())
    go(consumer())

    print("Waiting for everything to complete")
    await (exit >> _)
    print("All done, exiting!")
    # await asyncio.sleep(2)
    # print(f"Initial value: {v}")
    # await (c << 2)
    # await (c >> v)
    # # breakpoint()
    # print(c._channel.qsize())
    # print(f"Value received from a channel: {v}")


if __name__ == "__main__":
    asyncio.run(main())    
