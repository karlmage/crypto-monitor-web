from flask import Flask, Blueprint, render_template, jsonify, current_app
from app.services.coingecko import CoingeckoNotFound, CoingeckoError, CoingeckoRateLimit

main = Blueprint('main', __name__)

@main.route('/home')
@main.route('/')
def index():
    return render_template("index.html")

@main.route('api/<coin_id>/price')
def price(coin_id):
    # return f"{coin_id}: {get_price(coin_id=coin_id)}"
    client = current_app.extensions["coingecko"]
    currency = current_app.config.get("DEFAULT_CURRENCY", "usd")

    try:
        price_value = client.get_price(coin_id=coin_id, currency=currency)
        return jsonify({"coin_id": coin_id, "currency": currency, "price": price_value})
    except CoingeckoNotFound:
        return jsonify({"error": "Coingecko not found"}), 404
    except CoingeckoRateLimit:
        return jsonify({"error": "Coingecko rate limit exceeded"}), 429
    except CoingeckoError as e:
        current_app.logger.exception("Coingecko error: %s", e)
        return jsonify({"error": "Upstream error"}), 503
