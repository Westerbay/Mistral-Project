from model import AIModel

class AIDevHelper(AIModel):

    def __init__(self, mistral_model, api_key):
        AIModel.__init__(self, mistral_model, api_key)

    def prefixPrompt(self):
        return "I will give you a part of a code, can you explain it step by step, try to optimize it and generate unit tests ?"

    