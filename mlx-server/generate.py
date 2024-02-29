from mlx_lm.utils import load, generate_step
import mlx.core as mx
import re

model, tokenizer = load("mlx-community/Nous-Hermes-2-Mistral-7B-DPO-4bit-MLX")

temperature = 0
context_length = 1000
stop_words = ["<|im_start|>", "<|im_end|>", "<s>", "</s>"]
prompt="write me a poem about the ocean"


def generate_steps(the_prompt, the_model):
    tokens = []
    skip = 0

    for (token, prob), n in zip(generate_step(mx.array(tokenizer.encode(the_prompt)), the_model, temperature),
                                range(context_length)):

        if token == tokenizer.eos_token_id:
            break

        tokens.append(token.item())
        text = tokenizer.decode(tokens)

        trim = None

        for sw in stop_words:
            if text[-len(sw):].lower() == sw:
                return
            else:
                for i, _ in enumerate(sw, start=1):
                    if text[-i:].lower() == sw[:i]:
                        trim = -i

        yield text[skip:trim]
        skip = len(text)


def generate(prompt, model2):
    response = ''
    for chunk in generate_steps(prompt, model):
        print(chunk)
        response = response + chunk
        if True:
            response = re.sub(r"^/\*+/", "", response)
            response = re.sub(r"^:+", "", response)
            response = response.replace('�', '')

    print(response)
    return response