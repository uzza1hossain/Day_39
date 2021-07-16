import requests
import os

SHETTY_PRICES_ENDPOINTS = os.environ["SHETTY_PRICE_ENDPOINTS"]
SHETTY_USER_ENDPOINT = os.environ["SHETTY_USER_ENDPOINT"]


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHETTY_PRICES_ENDPOINTS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{SHETTY_PRICES_ENDPOINTS}/{city['id']}", json=new_data)

    def get_customer_emails(self):
        response = requests.get(url=SHETTY_USER_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data



