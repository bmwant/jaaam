import asyncio


async def my_coroutine():
    # your asyncio code here
    await asyncio.sleep(1)
    print("First finished")


async def my_other_coroutine():
    # your other asyncio code here
    await asyncio.sleep(0.1)
    print("Other finished")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine())
    loop.run_until_complete(my_other_coroutine())


if __name__ == "__main__":
    main()