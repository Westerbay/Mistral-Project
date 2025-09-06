from model import AIModel
from devhelper import AIDevHelper
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

import uvicorn


class Application:

    MODELS = {
        "chat": AIModel,
        "dev": AIDevHelper
    }
    PORT = 8000
    HOST = "localhost"

    def __init__(self, mistral_model, api_key):
        self.models = {
            model: self.MODELS[model](mistral_model, api_key) for model in self.MODELS
        }
        self.current_model_type = "chat"
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
        self._add_routes()

    def get_current_model(self):
        return self.models[self.current_model_type]
    
    def run(self):
        uvicorn.run(self.app, host=self.HOST, port=self.PORT, reload=False)

    def _add_routes(self):
        @self.app.post("/request")
        async def request(prompt: str = Body(..., embed=True)):
            response = self.get_current_model().request(prompt)
            return {"response": response}

        @self.app.post("/change_model")
        async def change_model(model_type: str = Body(..., embed=True)):
            if model_type not in self.MODELS:
                return {"status": "KO"}
            else:
                self.current_model_type = model_type
                return {"status": "OK"}

        @self.app.post("/get_models")
        async def get_models():
            return {"models": list(self.MODELS.keys())}       
    
