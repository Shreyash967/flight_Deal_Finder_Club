#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
import requests_cache
from datetime import timedelta , datetime 
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager

requests_cache.install_cache('flight_club_cache', urls_expire_after={ "*.sheety.co*": requests_cache.DO_NOT_CACHE,"*": 3600,})

flight_search = FlightSearch()
dm = DataManager()
 

sheet_data = dm.destination_price()
customers_data = dm.get_customers_email()
customers_email = [customer["email"] for customer in customers_data]


tommorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

# Set your origin airport (London Heathrow)
ORIGIN_CITY_IATA = "LHR"

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tommorrow,
        to_time=six_months_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" :
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tommorrow,
            to_time=six_months_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: GBP {cheapest_flight.price}")

notification_manager = NotificationManager()
notification_manager.send_mail(
    message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
    f"on {cheapest_flight.out_date} with {cheapest_flight.stops} stop(s)."
    , email=customers_email
    )
