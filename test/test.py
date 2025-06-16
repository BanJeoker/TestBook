import asyncio

shared_counter = 0

async def increment():
    global shared_counter
    temp = shared_counter
    await asyncio.sleep(0.1)  # Simulate some delay
    shared_counter = temp + 1

async def main():
    await asyncio.gather(increment(), increment(), increment())

await main()
print("Final counter:", shared_counter)

