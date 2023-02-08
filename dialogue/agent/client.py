import asyncio

from dialogue.agent.base import AgentID, Agent
from dialogue.main import MessagePump


class Client(Agent):
    def __init__(self, queue: MessagePump, agent_id: AgentID):
        super().__init__(queue, agent_id)
        self.queries = ["this", "that", "more", "end"]
        self.queries_iter = iter(self.queries)

    async def run(self):
        self._polling_task = asyncio.create_task(
            self.wait_message_from(AgentID.SHOP)
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
