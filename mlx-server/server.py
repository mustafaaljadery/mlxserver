from flask import Flask
from generate import generate

class MLXServer:
    def __init__(self):
        self.app = Flask(__name__)
    
        @self.app.route('/')
        def hello():
            return generate("Write me a poem about earth", "mlx-community/Nous-Hermes-2-Mistral-7B-DPO-4bit-MLX")
        
        self.app.run(debug=True)