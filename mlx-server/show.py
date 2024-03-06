from huggingface_hub import ModelCard

def show(model):
    return str(ModelCard.load(model))