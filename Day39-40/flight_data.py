class FlightData:
    """class of flight data, it is created in each flight search query"""
    def __init__(self, price, from_city, from_airport,
                 destination_city, destination_airport, trip_date, return_date):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.trip_date = trip_date
        self.return_date = return_date

    def print_data(self):
        print(f'''price : {self.price}
        {self.from_city} = from_city
        {self.from_airport} = from_airport
        {self.destination_city} = destination_city
        {self.destination_airport} = destination_airport
        {self.trip_date} = trip_date
        {self.return_date} = return_date''')
