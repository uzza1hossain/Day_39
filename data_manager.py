from pprint import pprint
import requests
import os

SHETTY_PRICES_ENDPOINTS = "https://api.sheety.co/b5350f4d803f9cdcc67600d6cbdc012d/flightDeals/prices"



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



