from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta

load_dotenv()

TEQUILA_FLIGHT_SEARCH_API_ENDPOINT = os.getenv("TEQUILA_FLIGHT_SEARCH_API_ENDPOINT")
TEQUILA_FLIGHT_LOCATIONS_API_ENDPOINT = os.getenv("TEQUILA_FLIGHT_LOCATIONS_API_ENDPOINT")
TEQUILA_FLIGHT_API_KEY = os.getenv("TEQUILA_FLIGHT_API_KEY")

date_now = datetime.now()
tomorrow = (date_now + timedelta(days=1)).strftime("%d/%m/%Y")
date_in_six_months = (date_now + timedelta(days=(30 * 6))).strftime("%d/%m/%Y")


class FlightSearch:
    
    def __init__(self, fly_from: str = "LAX", date_from: str = None, date_to: str = None) -> None:
        self.fly_from = fly_from
        self.date_from = tomorrow
        self.date_to = date_in_six_months

    def get_city_code(self, term: str):
        endpoint = f"{TEQUILA_FLIGHT_LOCATIONS_API_ENDPOINT}/locations/query"

        headers = {
            "apikey": TEQUILA_FLIGHT_API_KEY
        }

        parameters = {
            "term": term,
            "location_types": "city"
        }

        response = requests.get(url=endpoint, headers=headers, params=parameters)
        response.raise_for_status()

        data = response.json()
        city_code = data["locations"][0]["code"]

        print(city_code)
        return city_code

    def search_flights(self, fly_to: str, date_to: str = None, fly_from: str = None, date_from: str = None, sort: str = "date"):
        endpoint = f"{TEQUILA_FLIGHT_SEARCH_API_ENDPOINT}/search"

        headers = {
            "apikey": TEQUILA_FLIGHT_API_KEY
        }

        parameters = {
            "fly_from": fly_from if fly_from else self.fly_from,        # Usually it's the airport's IATA
            "fly_to": fly_to,                                           # Usually it's the airport's IATA
            "date_from": date_from if date_from else self.date_from,    # (dd/mm/yyyy)
            "date_to": date_to if date_to else self.date_to,            # (dd/mm/yyyy)
            "sort": sort                                                # sorts the results by quality, price, date or duration. Date is the default value.
        }

        response = requests.get(url=endpoint, headers=headers, params=parameters)
        response.raise_for_status()

        data = response.json()
        return data

