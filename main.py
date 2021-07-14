# Day 39 starting
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime

# flight_data = FlightData()
notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1))
six_months = (datetime.datetime.now() + datetime.timedelta(days=(6 * 30)))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months,
    )

    try:
        if destination["lowestPrice"] < flight.price:
            message = f"Low price alert! Only {flight.price} fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
            notification_manager.send_notifications(message)
    except AttributeError:
        pass




