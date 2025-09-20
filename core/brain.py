import os, json, openai

class TradingBrain:
    """
    AI Brain: Self-rebuilding via LLM prompts
    """
    def __init__(self, rpc, security):
        self.rpc = rpc
        self.security = security
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def decide(self, market_data):
        """
        LLM decision engine
        """
        prompt = f"""
        Market snapshot: {json.dumps(market_data)}

        Goal: Maximize safe profit with minimal latency.
        Return JSON:
        {{
          "action": "buy/sell/hold",
          "token": "symbol",
          "amount": "float",
          "confidence": "0-1"
        }}
        """

        safe_prompt = self.security.filter_prompt(prompt)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role":"system","content":"You are a trading strategist."},
                          {"role":"user","content":safe_prompt}]
            )
            decision = json.loads(response["choices"][0]["message"]["content"])
            return decision
        except Exception as e:
            return {"action":"hold","error":str(e)}
