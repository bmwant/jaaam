import asyncio
from enum import IntEnum, auto

import click
from dialogue.main import MessagePump, Message


class AgentID(IntEnum):
    SHOP = auto()
    CLIENT = auto()


class Agent:
    ICON = ""
    COLOR = "cyan"
    NAME = "Agent"
    POLLING_DELAY = 0.1

    def __init__(self, queue: MessagePump, agent_id: AgentID):
        self.queue = queue
        self.agent_id = agent_id
        self._done : bool = False
        self._message = None
        self._polling_task = None

    async def wait_message_from(self, agent_id=None):
        while True:
            message : Message = await self.queue.peek()
            if message is not None and message.agent_id == agent_id:
                self._message = await self.queue.get()
            await asyncio.sleep(self.POLLING_DELAY)

    async def say(self, text: str):
        self.print(text)
        await self.queue.put(
            Message(agent_id=self.agent_id, text=text)
        )

    def print(self, text: str):
        name = click.style(f"{self.NAME}", fg=self.COLOR, bold=True)
        message = f"{self.ICON} {name}: {text}"
        click.echo(message)
