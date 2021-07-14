import datetime
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "bRFIy_maJip1WPnLV1h5VCG5xCHldNIj"

class FlightData:

    def __init__(self):
        self.price = 0
        self.departure_airport_code = "LON"
        self.departure_city = "LONDON"

    def get_flight_data(self, city_code="PAR"):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        search_headers = {"apikey": TEQUILA_API_KEY}
        time_now = datetime.datetime.now()
        tomorrow = (time_now + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (time_now + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
        six_months_7day = (time_now + datetime.timedelta(days=187)).strftime("%d/%m/%Y")
        six_months_28day = (time_now + datetime.timedelta(days=228)).strftime("%d/%m/%Y")
        search_params = {
            "fly_from": self.departure_airport_code,
            "fly_to": city_code,
            "date_from": tomorrow,
            "date_to": six_months,
            "return_from": six_months_7day,
            "return_to": six_months_28day,
            "curr": "GBP",
        }

        response = requests.get(url=search_endpoint, params=search_params, headers=search_headers)
        return response.json()
