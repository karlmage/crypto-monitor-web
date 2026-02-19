import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    DEBUG = False
    API_TIMEOUT = 5
    COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")

class DevelopmentConfig(BaseConfig):
    DEBUG = True