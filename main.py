#!/usr/bin/env python3
# demo runner for ai-chatbot (safe simulation only)

import time, random, uuid

class SelfRebuildingChatbot:
    def __init__(self):
        self.version = "1.0.0"
        print("Chatbot initialized, version", self.version)

    def detect_opportunity(self):
        id = str(uuid.uuid4())[:8]
        profit = round(random.uniform(0.1, 3.0), 2)
        print(f"Opportunity {id} found — est. profit {profit}")
        return {"id": id, "profit": profit}

    def deploy_replicant(self, opportunity):
        rid = str(uuid.uuid4())[:6]
        print(f"Replicant {rid} deployed for {opportunity['id']}")
        return rid

    def self_rebuild(self):
        major, minor, patch = map(int, self.version.split("."))
        self.version = f"{major}.{minor}.{patch+1}"
        print("Self-rebuilt to version", self.version)

    def run(self):
        print("Starting demo. Press Ctrl+C to stop.")
        try:
            while True:
                opp = self.detect_opportunity()
                self.deploy_replicant(opp)
                if random.random() > 0.7:
                    self.self_rebuild()
                time.sleep(2)
        except KeyboardInterrupt:
            print("Demo stopped.")

if __name__ == "__main__":
    SelfRebuildingChatbot().run()
