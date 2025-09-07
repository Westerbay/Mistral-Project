from dotenv import load_dotenv
from app import Application

import os


if __name__ == "__main__":
    load_dotenv()

    mistral_model = os.getenv("MISTRAL_MODEL", "mistral-large-latest")
    api_key = os.getenv("MISTRAL_API_KEY", "")
    
    host = "localhost"
    port = 8000

    application = Application(mistral_model, api_key, host, port)
    application.run()    
    