from pydantic_settings import BaseSettings, SettingsConfigDict

# constants
from .constants import ENV_FILE


class Settings(BaseSettings):
    """Configurações principais"""

    # Configurações básicas
    NAME: str = "Python NLP"
    VERSION: str = "1.0"

    # Controle do Normalize
    SET_LOWER_TEXT: bool = True
    SET_NO_ACCENTS: bool = True
    SET_WHITESPACES: bool = True

    model_config = SettingsConfigDict(
        env_file=ENV_FILE
    )


settings = Settings()
