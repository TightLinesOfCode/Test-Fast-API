from pydantic import BaseSettings

import json


class Config(BaseSettings):
    polygon_test_url: str

    class Config:
        case_sensitive = True