# Day 39 starting
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime

ORIGIN_CITY_IATA = "LON"

notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()

sheet_data = data_manager.get_destination_data()

# Check if IATA CODE is missing. If missing add IATA CODE for missing cities
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

# Search available flight for all destination
tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1))
six_months = (datetime.datetime.now() + datetime.timedelta(days=(6 * 30)))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months,
    )

    if flight is None:
        continue

    # If price is below then given price send notification to all users
    if destination["lowestPrice"] < flight.price:
        message = f"Low price alert! Only £{flight.price} fly from {flight.origin_city}-{flight.origin_airport}" \
                  f" to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over via {flight.via_city} City."

        customer_data = data_manager.get_customer_emails()
        emails = [row["email"]for row in customer_data]
        google_flight_link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}" \
                             f".{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}" \
                             f".{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_email(to_adds_list=emails, msg=message, link=google_flight_link)
        # notification_manager.send_sms(message, google_flight_link)
