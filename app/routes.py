from flask import Flask, Blueprint, render_template
from app.services.coingecko import get_price

main = Blueprint('main', __name__)

@main.route('/home')
@main.route('/')
def index():
    return render_template("index.html")

@main.route('/price/<coin_id>')
def price(coin_id):
    return f"{coin_id}: {get_price(coin_id=coin_id)}"
