import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)  # Simulates waiting (e.g., for API)
    print("...World!")

async def main():
    await say_hello()

asyncio.run(main())  # Kicks off the event loop
