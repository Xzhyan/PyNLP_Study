import re


class Tokenizer:
    """Separar todo o texto em tokens"""

    @staticmethod
    def split_text(text: str) -> list:
        """Separa cada palavra, letra e número do texto"""

        return re.findall(r"\w+|[^\w\s]", text)

    def tokenize(self, text: str) -> list:
        """Separa e retorna os tokens"""

        tokens = self.split_text(text)

        return tokens
        
