import re
import asyncio
from typing import List

from dialogue.agent.base import AgentID, Agent
from dialogue.main import MessagePump


class Client(Agent):
    ICON = "🚙"
    NAME = "Guest"
    COLOR = "magenta"

    def __init__(self, queue: MessagePump, agent_id: AgentID, queries: List[str]):
        super().__init__(queue, agent_id)
        self.queries = queries
        self.queries_iter = iter(self.queries)

    async def run(self):
        asyncio.create_task(
            self.wait_message_from(AgentID.SHOP)
        )
        while True:
            if self._done:
                break
            
            if self._message is not None:
                await self.handle(self._message)
            else:
                await asyncio.sleep(self.POLLING_DELAY)
    
        # self._polling_task.cancel()
        print("Client agent task is finished")

    def get_next_query(self) -> str:
        query = next(self.queries_iter)
        return query.strip().lower()

    async def handle(self, message):
        # NOTE: client does not actually handle messages from shop :)
        try:
            query = next(self.queries_iter).strip()
            query_normalized = query.lower()
            wait_pattern = re.compile(r"wait (\d+)\.")
            if match := wait_pattern.match(query_normalized):
                wait_seconds = int(match.groups()[0])
                await asyncio.sleep(wait_seconds)
                query = next(self.queries_iter).strip()

            await self.say(text=query)
            self._message = None
        except StopIteration:
            self._done = True
