from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
from .generate import generate, generate_steps
from .load import load_model
from .pull import pull
from .list import list
from .show import show
from .delete import delete
from .chat import chat, convert_chat

class MLXServer():
    def __init__(self, model, port = 5000):
        if model is None:
            raise ValueError("Model cannot be blank")

        self.app = Flask(__name__)
        CORS(self.app)
        self.model = model
        self.port = port 
        self.loaded_model, self.tokenizer = load_model(model)
    
        @self.app.route('/generate')
        def generate_endpoint():
            prompt = request.args.get("prompt")
            stream = request.args.get('stream') == 'true'
            if stream:
                return Response(stream_with_context(generate_steps(prompt, self.loaded_model, self.tokenizer)))
            else:
                return generate(prompt, self.loaded_model, self.tokenizer)
        
        @self.app.route("/chat", methods=['POST'])
        def chat_endpoint():
            messages = request.json.get("messages")
            stream = request.json.get('stream') == 'true'
            if stream: 
                prompt = convert_chat(messages)
                return Response(stream_with_context(generate_steps(prompt, self.loaded_model, self.tokenizer)))
            else: 
                return chat(messages, self.loaded_model, self.tokenizer) 

        @self.app.route("/list")
        def list_endpiont():
            return list()
        
        @self.app.route("/convert")
        def convert_endpoint():
            return "coming soon :)"

        @self.app.route("/delete")
        def delete_endpoint():
            model = request.args.get("model")
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