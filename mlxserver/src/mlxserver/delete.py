from .list import list
import os

def delete(model):
    cache_directory = os.path.expanduser("~/.cache/huggingface/hub/")
    files = list()

    if model not in files: 
        return "Error: File not found"
    
    file_path = os.path.join(cache_directory, "models--" + model)
    try:
        os.remove(file_path)
        return "File removed successfully."
    except PermissionError:
        return "Permission denied. Check your file permissions."
