from .normalize import Normalizer
from .tokenizer import Tokenizer


def nlp(text: str) -> list:
    """Processamento de linguagem natural"""

    normalizer = Normalizer()
    tokenizer = Tokenizer()

    processed_text = normalizer.normalize(text)
    processed_text = tokenizer.tokenize(text)    

    return processed_text
