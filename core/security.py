class SecurityManager:
    """
    Security Layer: prompt filtering, key mgmt
    """
    async def init(self):
        print("🔒 Security initialized")

    async def lockdown(self):
        print("🔒 Security lockdown")

    def filter_prompt(self, prompt):
        safe_keywords = ["trade","market","profit"]
        if not any(word in prompt for word in safe_keywords):
            raise ValueError("Unsafe prompt")
        return prompt
