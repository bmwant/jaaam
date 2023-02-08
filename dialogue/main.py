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


class Agent:
    POLLING_DELAY = 0.1

    def __init__(self, queue: MessagePump, agent_id: AgendID):
        self.queue = queue
        self.agent_id = agent_id
        self._done : bool = False
        self._message = None
        self._polling_task = None

    async def wait_message_from(self, agent_id=None):
        while True:
            # print(f"Waiting for.. {agent_id}")
            message : Message = await self.queue.peek()
            if message is not None and message.agent_id == agent_id:
                self._message = await self.queue.get()
            await asyncio.sleep(self.POLLING_DELAY)

    async def say(self, text: str):
        print(f"Agent {self.agent_id} is saying {text}")
        await self.queue.put(
            Message(agent_id=self.agent_id, text=text)
        )



class Client(Agent):
    def __init__(self, queue: MessagePump, agent_id: AgendID):
        super().__init__(queue, agent_id)
        self.queries = ["this", "that", "more", "end"]
        self.queries_iter = iter(self.queries)

    async def run(self):
        self._polling_task = asyncio.create_task(
            self.wait_message_from(AgendID.SHOP)
        )
        while True:
            if self._done:
                break
            
            if self._message is not None:
                await self.handle(self._message)
            else:
                await asyncio.sleep(self.POLLING_DELAY)
    
        self._polling_task.cancel()
        print("Client agent task is finished")

    async def handle(self, message):
        # NOTE: client does not actually handle messages from shop :)
        try:
            query = next(self.queries_iter)
            await self.say(text=query)
            self._message = None
        except StopIteration:
            self._done = True


class Shop(Agent):
    async def run(self):
        await self.say("Hello!")
        self._polling_task = asyncio.create_task(
            self.wait_message_from(AgendID.CLIENT)
        )
        while True:
            if self._done:
                break
    
            if self._message is not None:
                await self.handle(self._message)
            else:
                await asyncio.sleep(self.POLLING_DELAY)

        self._polling_task.cancel()
        print("Shop agent task is finished")

    async def handle(self, message: Message):
        print(f"Shop is processing {message}")
        # NOTE: waiting for the next message to arrive
        self._message = None
        await self.say(f"Did you ask {message.text}?")

        if message.text == "end":
            self._done = True


async def main():
    # NOTE: shared message queue to communicate between agents
    queue = MessagePump()
    # terminal = Terminal(queue=queue)
    client = Client(queue=queue, agent_id=AgendID.CLIENT)
    shop = Shop(queue=queue, agent_id=AgendID.SHOP)
    tasks = [
        # asyncio.create_task(terminal.run()),
        asyncio.create_task(shop.run()),
        asyncio.create_task(client.run()),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
