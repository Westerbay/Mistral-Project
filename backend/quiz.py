from model import AIModel

class AIQuiz(AIModel):

    def __init__(self, mistral_model, api_key):
        AIModel.__init__(self, mistral_model, api_key)

    def prefix_prompt(self):
        return "I will give you a topic. I want you to generate a quiz to test the knowledge on it."