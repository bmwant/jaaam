import asyncio

from dialogue.main import Message
from dialogue.agent.base import Agent, AgentID


class Shop(Agent):
    NAME = "Employee"
    COLOR = "yellow"

    async def run(self):
        await self.say("Hello!")
        self._polling_task = asyncio.create_task(
            self.wait_message_from(AgentID.CLIENT)
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
        text = message.text.lower()
        await self.say(f"Did you ask {text}?")

        if text == "that's all.":
            self._done = True
