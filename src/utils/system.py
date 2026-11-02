import json
from pathlib import Path

# nlp
from nlp import nlp


def read_json(json_path: Path):
    """Lê arquivos .json"""

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if not data:
                raise ValueError("Nenhum dado encontrado no .json")

            return data

    except FileNotFoundError as e:
        pass


def entry() -> str:
    """Recebe entradas do usuário"""

    # Controla o estado das entradas para detectar quando o usuário envidou dados ou não.
    empty = True

    while empty:
        entries = input(" @nlp > ")

        if entries:
            empty = False

    entries = nlp(text=entries)

    return entries

