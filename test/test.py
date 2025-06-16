import asyncio

async def greet(name):
    print(f"Hello, {name}")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}")

async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    )

await main()
