# Day 39 starting
from data_manager import DataManager
from flight_data import FlightData
flight_data = FlightData()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

else:
    for row in sheet_data:
        city_name = row["city"]
        city_code = row["iataCode"]
        price = flight_data.get_flight_data(city_code)
        price = price["data"][0]["price"]
        print(f"{city_name}: {price}")

    # print(f"{sheet_data}\n\n")
    # print(f"{sheet_data[0]['city']}\n\n")
