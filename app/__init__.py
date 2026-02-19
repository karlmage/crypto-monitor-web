from flask import Flask
from .config import DevelopmentConfig

def create_app(config_name = "development"):

    app = Flask(__name__)

    configs = {
        "development": DevelopmentConfig
    }

    app.config.from_object(configs[config_name])

    if not app.config.get("COINGECKO_API_KEY"):
        raise Exception("COINGECKO_API_KEY not set")

    from .routes import main
    app.register_blueprint(main, url_prefix="")

    return app
