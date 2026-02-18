from flask import Flask
from .config import DevelopmentConfig

def create_app(config_name = "development"):
    app = Flask(__name__)

    configs = {
        "development": DevelopmentConfig
    }

    app.config.from_object(configs[config_name])

    from .routes import main
    app.register_blueprint(main, url_prefix="")

    return app
