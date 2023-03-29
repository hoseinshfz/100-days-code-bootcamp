import requests
from flight_data import FlightData

FLIGHT_API = "****"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
headers = {"apikey": FLIGHT_API}


class FlightSearch:
    def __init__(self):
        self.flight_from = 'AMS'

    def iata_code_query(self, cities):
        """gets the IATA code of the missing cities"""
        codes = []
        for city in cities:
            if city['iataCode'] == '':
                city_name = city['city']
                query = {"term": city_name, "location_types": "city"}
                response = requests.get(url=location_endpoint, headers=headers, params=query)
                airport_code = response.json()['locations'][0]['code']
                codes.append((city['id'], airport_code))
        return codes

    def search_flights(self, from_city_code, destination_city, from_time, to_time):
        """search flights and returns FlightData"""
        flight_search_endpoint = f'{TEQUILA_ENDPOINT}/v2/search'
        query = {
                "fly_from": from_city_code,
                "fly_to": destination_city,
                "date_from": from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "EUR"
            }
        response = requests.get(url=flight_search_endpoint, headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            from_city=data["route"][0]["cityFrom"],
            from_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            trip_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0])

        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data

