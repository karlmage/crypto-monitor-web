class BaseConfig:
    DEBUG = False
    API_TIMEOUT = 5
    DEFAULT_CURRENCY = "usd"

class DevelopmentConfig(BaseConfig):
    DEBUG = True