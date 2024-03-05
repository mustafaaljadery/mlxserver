from server import MLXServer

mlx = MLXServer(
    model="mlx-community/Nous-Hermes-2-Mistral-7B-DPO-4bit-MLX"
)

mlx.generate("")