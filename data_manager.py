from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    
    def __init__(self) -> None:
        self.data = self.get_rows()

    def get_rows(self, row_number: int = None):
        """Retrieve rows from your sheet"""

        endpoint = f"{SHEETY_ENDPOINT}" if not row_number else f"{SHEETY_ENDPOINT}/{row_number}"

        headers = {
            "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
        }

        response = requests.get(url=endpoint, headers=headers)
        response.raise_for_status()

        data = response.json()["prices"]
        
        return data

    def add_row(self, city: str, iata: str, lowest_price: str):
        """Add a row to your sheet"""

        endpoint = f"{SHEETY_ENDPOINT}"

        headers = {
            "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
        }

        payload = {
            "price": {
                "city": city,
                "iataCode": iata,
                "lowestPrice": lowest_price,
            }
        }

        response = requests.post(url=endpoint, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()

        print(data)

    def edit_row(self, row_number: int, iata: str, city: str = None, lowest_price: str = None):
        """Edit a row in your sheet"""

        endpoint = f"{SHEETY_ENDPOINT}/{row_number}"

        headers = {
            "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
        }

        payload = {
            "price": {
                "city": city if city else None,
                "iataCode": iata,
                "lowestPrice": lowest_price if lowest_price else None,
            }
        }

        response = requests.put(url=endpoint, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()

        print(data)