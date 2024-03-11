from mlx_lm.utils import load, generate_step
import mlx.core as mx
import re

temperature = 0
context_length = 1000
stop_words = ["<|im_start|>", "<|im_end|>", "<s>", "</s>"]

def generate_steps(the_prompt, the_model, tokenizer):
    tokens = []
    skip = 0

    for (token, prob), n in zip(generate_step(mx.array(tokenizer.encode(the_prompt)), the_model, temperature),
                                range(context_length)):
        try:
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
        except:
            continue

def generate(prompt, model, tokenizer):
    response = ''

    for chunk in generate_steps(prompt, model, tokenizer):
        try:
            response = response + chunk
            if True:
                response = re.sub(r"^/\*+/", "", response)
                response = re.sub(r"^:+", "", response)
                response = response.replace('�', '')
        except:
            continue

    return response