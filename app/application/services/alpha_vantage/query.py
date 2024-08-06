from flask import current_app
import requests


class Query:
    """
    A class for querying the Alpha Vantage API.

    This class provides methods to make requests to the Alpha Vantage API,
    using an API key obtained from the Flask application's configuration.

    Attributes:
        api_key (str): The API key for accessing the Alpha Vantage API.
        api_url (str): The base URL for the Alpha Vantage API endpoint.

    Methods:
        execute(symbol: str, function: str) -> dict:
            Sends a request to the Alpha Vantage API with the given symbol and function.
            Returns the API response as a JSON dictionary.
    """

    def __init__(self):
        self.api_key = current_app.config["ALPHA_VANTAGE_API_KEY"]
        self.api_url = "https://www.alphavantage.co/query"

    def execute(self, symbol: str, function: str):
        params = {"function": function, "symbol": symbol, "apikey": self.api_key}
        response = requests.get(self.api_url, params=params, timeout=15)
        return response.json()
