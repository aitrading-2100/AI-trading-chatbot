from fastapi import FastAPI
import uvicorn

class Dashboard:
    def __init__(self, swarm):
        self.swarm = swarm
        self.app = FastAPI()

        @self.app.get("/status")
        def status():
            return {
                "replicants": len(self.swarm.replicants),
                "performance": self.swarm.ns.performance
            }

    async def serve(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8000)
