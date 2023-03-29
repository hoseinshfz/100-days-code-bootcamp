import requests
from pprint import pprint

sheety_url = "https://api.sheety.co/****/flightDeals"
sheety_price_url = f'{sheety_url}/prices'
sheety_user_url = f'{sheety_url}/users'
SHEETY_USERNAME = "***"
SHEETY_PASSWORD = "*****"

# to reduce the API requests to sheety, theses constant lists are created
CITIES = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
           {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},
           {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 685},
           {'city': 'Milan', 'iataCode': 'MIL', 'id': 5, 'lowestPrice': 551},
           {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 395},
           {'city': 'Toronto', 'iataCode': 'YTO', 'id': 7, 'lowestPrice': 414},
           {'city': 'London', 'iataCode': 'LON', 'id': 8, 'lowestPrice': 240}]

USERS = [{'firstName': 'test', 'lastName': 'temp', 'email': '***@gmail.com', 'id': 2},
         {'firstName': 'dragon', 'lastName': 'master', 'email': 'XXX@gmail.com', 'id': 3}]


class DataManager:
    """This class is responsible for talking to the Flight Club with Sheety Api"""
    def __init__(self):
        self.destination_cities = []
        self.users = []
        # Reading from sheets or constants
        self.read_price_sheet()
        self.read_user_sheet()
        # self.fill_data_from_constant()

    def fill_data_from_constant(self):
        self.destination_cities = CITIES
        self.users = USERS

    def read_price_sheet(self):
        """this functions read from prices sheet and write into self.destination_cities"""
        response = requests.get(url=sheety_price_url, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
        self.destination_cities = response.json()['prices']

    def read_user_sheet(self):
        """this functions read from users sheet and write into self.users"""
        response = requests.get(url=sheety_user_url, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
        self.users = response.json()['users']
        print(self.users)

    def get_users_data(self):
        return self.users

    def get_destination_cities(self):
        return self.destination_cities

    def update_destination_code(self, codes):
        """updates the IATA code field of the Flight Club's data sheet"""
        for item in codes:
            index = item[0]
            code = item[1]
            sheet_input = {
                'price': {
                    'iataCode': code
                }
            }
            self.destination_cities[index - 2]['iataCode'] = code
            prices_iota_endpoint = f'{sheety_price_url}/{index}'
            response = requests.put(url=prices_iota_endpoint,
                                    auth=(SHEETY_USERNAME, SHEETY_PASSWORD),
                                    json=sheet_input)
            print(response.text)
