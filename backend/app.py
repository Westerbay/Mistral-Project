from model import AIModel
from devhelper import AIDevHelper
from quiz import AIQuiz
from summarize import AISummarize
from translate import AITranslate

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import uvicorn


class Application:

    MODELS = {
        "AIModel": AIModel,
        "AIDevHelper": AIDevHelper,
        "AIQuiz": AIQuiz,
        "AISummarize": AISummarize,
        "AITranslate": AITranslate
    }

    def __init__(self, mistral_model, api_key, host, port):
        self.models = {
            model: self.MODELS[model](mistral_model, api_key) for model in self.MODELS
        }
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )        
        self.host = host
        self.port = port        
        self._add_routes()

    def get_model(self, model):
        return self.models[model]
    
    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port, reload=False)

    def _add_routes(self):
        @self.app.post("/request")
        async def request(prompt: str = Body(...), model: str = Body(...)):
            response = self.get_model(model).request(prompt)
            return {"text": response}

        @self.app.post("/get_models")
        async def get_models():
            return {"models": list(self.MODELS.keys())}     

        self.app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")  
    
