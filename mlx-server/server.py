import requests
from flask import Flask, request
from generate import generate
from load import load_model
from pull import pull
from list import list
from show import show
from delete import delete

class MLXServer:
    def __init__(self, model, port = 5000):
        if model is None:
            raise ValueError("Model cannot be blank")

        self.app = Flask(__name__)
        self.model = model
        self.port = port 

        self.loaded_model, self.tokenizer = load_model(model)
    
        @self.app.route('/generate')
        def generate_endpoint():
            prompt = request.args.get("prompt")
            return generate(prompt, self.loaded_model, self.tokenizer)
        
        @self.app.route("/chat")
        def chat_endpoint():
            return 
        
        @self.app.route("/list")
        def list_endpiont():
            return list()
        
        @self.app.route("/convert")
        def convert_endpoint():
            return "coming soon :)"

        @self.app.route("/delete")
        def delete_endpoint():
            model = request.args.get('model')
            return delete(model)

        @self.app.route("/pull")
        def pull_endpoint():
            model = request.args.get('model')
            return pull(model)

        @self.app.route("/show")
        def show_endpoint():
            model = request.args.get('model')
            return show(model)
        
        self.app.run(port=self.port)
    
    def generate(self, prompt):
        #requests.get(f"localhost:{self.port}")
        return
    
    def chat(self, messages):
        pass