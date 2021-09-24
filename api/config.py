from pydantic import BaseSettings


class Config(BaseSettings):
    POLYGON_REPOSITORY_URL: str

    class Config:
        case_sensitive = True