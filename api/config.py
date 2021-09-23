from pydantic import BaseConfig

class Config(BaseConfig):
    FINHUB_REPOSITORY_URL: str

    class Config:
        case_sensitive = True