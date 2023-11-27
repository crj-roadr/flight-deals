#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

def update_google_sheets_with_city_codes():
  for row in data_manager.data:
    city_code = flight_search.get_city_code(term=row["city"])
    data_manager.edit_row(row_number=row["id"], iata=city_code)

    print(f"Operation was successful")

def print_structured_flight_data():
  for row in data_manager.data:
    raw_flight_data = flight_search.search_flights(fly_to=row["iataCode"])
    structured_flight_data = FlightData(data_from_flight_search=raw_flight_data).data
    filtered_flight_data = [ data for data in structured_flight_data if float(data["price"]) < float(row["lowestPrice"]) ]

    if len(filtered_flight_data) > 0:
      message = f"Sent from your Twilio trial account - Low price alert! Prices lower than £{row["lowestPrice"]} to fly from {filtered_flight_data[0]["cityFrom"]}-{filtered_flight_data[0]["cityCodeFrom"]} to {filtered_flight_data[0]["cityTo"]}-{filtered_flight_data[0]["cityCodeTo"]}, from {filtered_flight_data[0]["local_departure"]} to {filtered_flight_data[-1]["local_departure"]}"
      notification_manager.send_sms(body=message)

print_structured_flight_data()