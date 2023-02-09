import asyncio
import click

from dialogue.main import MessagePump
from dialogue.agent import Shop, Client, AgentID


@click.group(invoke_without_command=False)
def cli():
    pass


@cli.command()
@click.argument("guest_input", type=click.File('r'))
def process(guest_input):
    """
    Processes converstation with a guest
    """
    queries = guest_input.readlines()
    async def entrypoint():
        # NOTE: shared message queue to communicate between agents
        queue = MessagePump()
        # terminal = Terminal(queue=queue)
        client = Client(
            queue=queue, 
            agent_id=AgentID.CLIENT,
            queries=queries,
        )
        shop = Shop(queue=queue, agent_id=AgentID.SHOP)
        tasks = [
            # asyncio.create_task(terminal.run()),
            asyncio.create_task(shop.run()),
            asyncio.create_task(client.run()),
        ]
        await asyncio.gather(*tasks)

    asyncio.run(entrypoint())


if __name__ == '__main__':
    """
    Usage:
    python cli.py process input.txt
    """
    cli()
