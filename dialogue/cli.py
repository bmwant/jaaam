import asyncio
import click

from hiauto.shop import Shop
from hiauto.agent import GuestAgent, EmployeeAgent


@click.group(invoke_without_command=False)
def cli():
    pass


@cli.command()
@click.argument("guest_input", type=click.File('r'))
def process(guest_input):
    """
    Processes converstation with a guest
    """
    guest = GuestAgent(name="Guest", queries=guest_input.readlines())
    employee = EmployeeAgent(name="Employee")
    shop = Shop(agents=[
        employee,
        guest,
    ])
    asyncio.run(shop.run())
    # click.echo(guest_input.read())



if __name__ == '__main__':
    """
    Usage:
    python cli.py process input.txt
    """
    cli()