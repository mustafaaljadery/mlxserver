# MLX Server

The easiest way to create a server to inference MLX models.

## Documentation

For documentation and guides, visit [mlxserver.com](https://mlxserver.com)

## Getting Started

Install `mlxserver` via pip to get started. This installation will install `mlx` as well.

### Install using PyPI

```bash copy
pip install mlxserver
```

To install from PyPI you must meet the following requirements:

- Using an M series chip (Apple silicon)
- Using a native Python >= 3.8
- macOS >= 13.3

### Usage

The following is an example of using `Mistral 7B Nous Hermes 2` for generating text:

**Python**

```python copy
from mlxserver import MLXServer

server = MLXServer(model="mlx-community/Nous-Hermes-2-Mistral-7B-DPO-4bit-MLX")
```

**Curl**

```bash copy
curl -X GET 'http://127.0.0.1:5000/generate?prompt=write%20me%20a%20poem%20about%the%20ocean&stream=true'
```

### Note

This library only runs on Apple Metal. The MLX library focuses on Apple Metal acceleration.
