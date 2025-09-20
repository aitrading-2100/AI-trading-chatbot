# demo runner for ai-trading-chatbot (testnet simulation only)
import asyncio, random

async def run_demo():
    print("Starting demo replicant (testnet simulation only)")
    for i in range(5):
        price = random.uniform(100, 200)
        print(f"[demo] tick {i+1}: price={price:.2f}")
        await asyncio.sleep(1)
    print("Demo finished")

if __name__ == "__main__":
    asyncio.run(run_demo())
