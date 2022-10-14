from pydantic import BaseSettings


class BotConfig(BaseSettings):
    token: str
    dsn: str
    redis_storage: bool = False
    echo: bool = False

    class Config:
        case_sensitive = False
        env_prefix = 'bot_'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = "__"
