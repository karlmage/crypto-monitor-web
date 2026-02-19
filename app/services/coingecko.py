#Coingecko API: https://docs.coingecko.com/
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("COINGECKO_API_KEY")

url = "https://pro-api.coingecko.com/api/v3/ping"

headers = {"x-cg-pro-api-key": f"{api_key}"}

response = requests.get(url, headers=headers)

print(response.json())