#Coingecko API: https://docs.coingecko.com/
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("COINGECKO_API_KEY")
headers = {"x-cg-demo-api-key": api_key}

def get_price(coin_id, currency = "usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies={currency}&ids={coin_id}"
    response = requests.get(url, headers=headers)
    return response.json()[coin_id][currency]

print(get_price(coin_id = "bitcoin", currency = "usd"))
