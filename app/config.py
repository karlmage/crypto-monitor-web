import os

class BaseConfig:
    DEBUG = False
    API_TIMEOUT = 5
    COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
    DEFAULT_CURRENCY = "usd"

class DevelopmentConfig(BaseConfig):
    DEBUG = True