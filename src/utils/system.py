

# nlp
from nlp import nlp


def entry() -> str:
    """Recebe entradas do usuário"""

    empty = True

    while empty:
        entries = input(" @nlp > ")

        if entries:
            empty = False

    entries = nlp(text=entries)

    return entries

