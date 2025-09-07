from model import AIModel

class AITranslate(AIModel):

    def __init__(self, mistral_model, api_key):
        AIModel.__init__(self, mistral_model, api_key)

    def prefix_prompt(self):
        return "I will give you a text to translate in english if I don't mention the language output, otherwise translate it in the mentionned language."

    