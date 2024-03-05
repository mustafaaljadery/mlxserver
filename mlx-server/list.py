import os

def list():
    cache_directory = os.path.expanduser("~/.cache/huggingface/hub/")
    files = [file[8:] for file in os.listdir(cache_directory) if file.startswith("models--")]
    return files