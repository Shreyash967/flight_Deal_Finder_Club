import os
from dotenv import load_dotenv
import requests
import json 
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("serpapi")
        self.endpoint = "https://serpapi.com/search.json"

    def check_flights(self , origin_city_code, destination_city_code, from_time, to_time , is_direct=True):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.api_key,
        }

        if is_direct:
            query["stops"] = "1"


        response = requests.get(self.endpoint, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        
        return data
