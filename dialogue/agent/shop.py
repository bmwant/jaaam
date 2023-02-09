import asyncio
import time

from dialogue.main import Message, MessagePump
from dialogue.agent.base import Agent, AgentID


go = asyncio.create_task

class Shop(Agent):
    NAME = "Employee"
    ICON = "🍔"
    COLOR = "yellow"
    WAITING_DELAY = 5

    def __init__(self, queue: MessagePump, agent_id: AgentID):
        super().__init__(queue, agent_id)
        self._wait_client : bool = False
        self._last_response = time.monotonic()

    async def run(self):
        await self.say("Hello!")
        
        go(self.wait_message_from(AgentID.CLIENT))

        while True:
            if self._done:
                break
    
            if self._message is not None:
                await self.handle(self._message)
            else:
                await asyncio.sleep(self.POLLING_DELAY)

        print("Shop agent task is finished")

    async def wait_decision(self):
        while True:
            if self._done or not self._wait_client:
                return

            await asyncio.sleep(self.WAITING_DELAY)
            await self.say("Please let me know when you are ready.\n")

    async def handle(self, message: Message):
        print(f"Shop is processing {message}")
        # NOTE: waiting for the next message to arrive
        self._message = None
        text = message.text.lower()
        # We've got some query
        self._wait_client = False

        await self.say(f"Did you ask {text}?")

        match text:
            case "let me think.":
                self._wait_client = True
                go(self.wait_decision())
            case "that's all.":
                self._done = True

        
