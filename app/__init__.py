from flask import Flask
from .config import DevelopmentConfig
from .services.coingecko import CoingeckoClient
from dotenv import load_dotenv
from pathlib import Path
import os

def create_app(config_name = "development"):

    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)

    app = Flask(__name__)

    configs = {
        "development": DevelopmentConfig
    }

    app.config.from_object(configs[config_name])
    app.config["COINGECKO_API_KEY"] = os.getenv("COINGECKO_API_KEY")

    if not app.config.get("COINGECKO_API_KEY"):
        raise Exception("COINGECKO_API_KEY not set")

    app.extensions["coingecko"] = CoingeckoClient(
        api_key = app.config["COINGECKO_API_KEY"],
        timeout = app.config.get("API_TIMEOUT", 5),
    )

    from .routes import main
    app.register_blueprint(main, url_prefix="")

    return app
