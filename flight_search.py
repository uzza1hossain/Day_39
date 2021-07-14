import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "bRFIy_maJip1WPnLV1h5VCG5xCHldNIj"

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        search_params = {
            "term": city_name,
            "location_types": "city"
        }
        search_headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(url=location_endpoint, params=search_params,
                                 headers=search_headers)
        code = response.json()["locations"][0]["code"]
        return code



