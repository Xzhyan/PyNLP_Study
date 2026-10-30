import unicodedata


from core import settings


class Normalizer:
    """Normaliza todo o texto de entrada"""

    @staticmethod
    def lower_text(text: str) -> str:
        """Transforma o texto de entrada em letras minúsculas"""

        return text.lower()

    @staticmethod
    def remove_accents(text: str) -> str:
        """Remove os acentos desnecessários como (~^)"""

        text = unicodedata.normalize("NFD", text)
        text = "".join(
            char for char in text if unicodedata.category(char) != "Mn"
        )

        return text

    @staticmethod
    def whitespace(text: str) -> str:
        """Remove os espaços em branco duplicados"""

        return " ".join(text.split())

    def normalize(self, text: str) -> str:
        """Conforme as configurações, normaliza o texto"""

        if settings.SET_LOWER_TEXT:
            text = self.lower_text(text)

        if settings.SET_NO_ACCENTS:
            text = self.remove_accents(text)

        if settings.SET_WHITESPACES:
            text = self.whitespace(text)

        return text
