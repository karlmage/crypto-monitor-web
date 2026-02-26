#Coingecko API: https://docs.coingecko.com/
import requests

class CoingeckoError(Exception):
    pass

class CoingeckoRateLimit(CoingeckoError):
    pass

class CoingeckoNotFound(CoingeckoError):
    pass

class CoingeckoClient:
    BASE_URL = "https://api.coingecko.com/api/v3/"

    def __init__(self, api_key: str | None, timeout: int = 5):
        self.timeout = timeout
        self.session = requests.Session()
        self.headers = {}
        if api_key:
            self.headers["x-cg-demo-api-key"] = api_key

    def get_price(self, coin_id: str, currency: str = "usd") -> float:
        url = f"{self.BASE_URL}/simple/price"
        params = {"vs_currencies": currency, "ids": coin_id}

        try:
            response = self.session.get(url, params=params, headers=self.headers, timeout=self.timeout)
        except requests.RequestException as e:
            raise CoingeckoError(f"Network error: {e}") from e

        if response.status_code == 429:
            raise CoingeckoRateLimit("Rate limit exceeded")
        if response.status_code >= 500:
            raise CoingeckoError(f"Upstream error: {response.status_code}")

        try:
            response.raise_for_status()
            data = response.json()
        except ValueError as e:
            raise CoingeckoError("Invalid JSON from Coingecko") from e
        except requests.HTTPError as e:
            raise CoingeckoError(f"HTTP error: {response.status_code}") from e

        if coin_id not in data or currency not in data[coin_id]:
            raise CoingeckoNotFound(f"Price not found for coin_id={coin_id}")

        return float(data[coin_id][currency])

