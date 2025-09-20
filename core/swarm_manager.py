import asyncio
from core.replicant import Replicant
from core.ml_nervous_system import NervousSystem

class SwarmManager:
    def __init__(self, brain, rpc, security):
        self.brain = brain
        self.rpc = rpc
        self.security = security
        self.ns = NervousSystem()
        self.replicants = []

    async def run(self):
        for _ in range(3):
            await self.spawn_replicant()

        while True:
            losers = self.ns.prune_replicants()
            for rid in losers:
                self.kill_replicant(rid)
                await self.spawn_replicant()
            await asyncio.sleep(5)

    async def spawn_replicant(self):
        r = Replicant(self.brain, self.rpc, self.security, self.ns)
        self.replicants.append(r)
        asyncio.create_task(r.run())
        print(f"🚀 Spawned Replicant {r.id}")

    def kill_replicant(self, rid):
        for r in self.replicants:
            if r.id == rid:
                r.alive = False
                print(f"💀 Killed Replicant {r.id}")
                self.replicants.remove(r)
                break
