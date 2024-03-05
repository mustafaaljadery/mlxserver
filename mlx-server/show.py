from huggingface_hub import ModelCard

def show(model):
    return ModelCard.load(model)