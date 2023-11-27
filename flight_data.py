from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, data_from_flight_search) -> None:
        self.data = self.structure_data(data_from_flight_search)

    def structure_data(self, data_from_flight_search):
        data = [ { "local_departure": data["local_departure"].split("T")[0], "cityFrom": data["cityFrom"], "cityCodeFrom": data["cityCodeFrom"], "cityTo": data["cityTo"], "cityCodeTo": data["cityCodeTo"], "price" :data["price"]} for data in data_from_flight_search["data"] ]
        return data