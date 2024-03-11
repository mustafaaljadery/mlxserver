from huggingface_hub import snapshot_download
import time

def pull(model):
    start_time = time.time()
    snapshot_download(model)
    end_time = time.time()
    return {"time": f"{end_time - start_time} seconds"}
