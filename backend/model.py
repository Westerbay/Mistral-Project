from mistralai import Mistral

import random


class AIModel:

    def __init__(self, mistral_model, api_key):
        self.mistral_model = mistral_model
        self.client = Mistral(api_key=api_key)

    def prefix_prompt(self):
        return ""

    def suffix_prompt(self):
        return ""

    def request(self, prompt):
        complete_prompt = self.prefix_prompt() + "\n" + prompt
        complete_prompt += "\n" + self.suffix_prompt()
        try:
            chat_response = self.client.chat.complete(
                model = self.mistral_model,
                messages = [
                    {
                        "role": "user",
                        "content": complete_prompt
                    },
                ]
            )
            response_choice = random.choice(chat_response.choices)
            return response_choice.message.content
        except Exception as e:
            return "Missing or invalid MISTRAL_MODEL or MISTRAL_API_KEY\n" + str(e)
