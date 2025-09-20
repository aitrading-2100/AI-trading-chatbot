import asyncio
from core.brain import TradingBrain
from core.swarm_manager import SwarmManager
from core.security import SecurityManager
from infra.rpc_manager import RPCManager
from monitoring.dashboard import Dashboard

class EnterpriseTradingBot:
    def __init__(self):
        self.security = SecurityManager()
        self.rpc = RPCManager()
        self.brain = TradingBrain(self.rpc, self.security)
        self.swarm = SwarmManager(self.brain, self.rpc, self.security)
        self.dashboard = Dashboard(self.swarm)

    async def start(self):
        print("🚀 Starting Enterprise AI Trading Chatbot")
        await self.security.init()
        await self.rpc.connect()

        await asyncio.gather(
            self.swarm.run(),
            self.dashboard.serve()
        )

    async def stop(self):
        print("🛑 Stopping Enterprise Bot")
        await self.rpc.disconnect()
        await self.security.lockdown()

if __name__ == "__main__":
    bot = EnterpriseTradingBot()
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        asyncio.run(bot.stop())
