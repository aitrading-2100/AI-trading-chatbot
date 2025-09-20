import asyncio, uuid, random
from web3 import Web3

class Replicant:
    """
    Autonomous Replicant Bot
    """
    def __init__(self, brain, rpc, security, nervous_system):
        self.id = str(uuid.uuid4())[:8]
        self.brain = brain
        self.rpc = rpc
        self.security = security
        self.ns = nervous_system
        self.alive = True

    async def run(self):
        while self.alive:
            market_data = await self.rpc.get_market_data()
            decision = await self.brain.decide(market_data)

            if not self.ns.validate_decision(decision):
                await asyncio.sleep(0.5)
                continue

            profit = await self.execute_trade(decision)
            self.ns.reward(self.id, profit)

            await asyncio.sleep(1)

    async def execute_trade(self, decision):
        """
        Real Web3 execution (swap simulation).
        """
        try:
            if decision["action"] == "hold":
                return 0.0

            # Gas simulation
            gas_cost = random.uniform(0.0001, 0.001)
            profit = random.uniform(-0.05, 0.15) - gas_cost

            print(f"[{self.id}] {decision['action']} {decision['token']} → Profit: {profit:.4f}")
            return profit

        except Exception as e:
            print(f"[{self.id}] Trade failed: {e}")
            return -0.01
