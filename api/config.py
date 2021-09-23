from pydantic import BaseConfig

class Config(BaseConfig):
    POLYGON_REPOSITORY_URL: str

    class Config:
        case_sensitive = True