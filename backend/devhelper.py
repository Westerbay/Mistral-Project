from model import AIModel

class AIDevHelper(AIModel):

    def __init__(self, mistral_model, api_key):
        AIModel.__init__(self, mistral_model, api_key)

    def prefix_prompt(self):
        return "I will give you a piece of code. Explain it step by step, optimize it, and write unit tests."

    