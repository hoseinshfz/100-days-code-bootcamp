import requests
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

FROM_CITY_IATA = "AMS"

data_manager = DataManager()
flight_searcher = FlightSearch()
notification_manager = NotificationManager()

cities = data_manager.get_destination_cities()
price_alert = {city['city']: city['lowestPrice'] for city in cities}

iata_codes = flight_searcher.iata_code_query(cities)
if len(iata_codes) > 0:
    data_manager.update_destination_code(iata_codes)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
flights = []
for destination_city in cities:
    res = flight_searcher.search_flights(from_city_code=FROM_CITY_IATA,
                                         destination_city=destination_city['iataCode'],
                                         from_time=tomorrow,
                                         to_time=six_month_from_today
                                         )
    flights.append(res)

message_list = []
for flight in flights:
    dest_city = flight.destination_city
    if flight.price < price_alert[dest_city]:
        message = f"Low price alert! Only €{flight.price} to fly from {flight.from_city}-{flight.from_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}, from {flight.trip_date} to {flight.return_date}."

        notification_manager.telegram_bot_send_text(message)
        message_list.append(message)
users_data = data_manager.get_users_data()
for user in users_data:
    notification_manager.send_email(user['email'], message_list)
