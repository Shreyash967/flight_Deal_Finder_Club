from dotenv import load_dotenv
import os
import requests 
load_dotenv()
sheety_api = os.getenv("sheety_api1")
sheet2_api = os.getenv("sheet2_api")
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(sheety_api)
        self.response.raise_for_status()
        

    def destination_price(self):
        data = self.response.json()
        return data["sheet1"]

    def update_price(self, row_id, new_price):
        update_endpoint = f"{sheety_api}/{row_id}"
        update_data = {
            "sheet1": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(update_endpoint, json=update_data)
        response.raise_for_status()
        return response.json()

    def get_customers_email(self):
        response = requests.get(url=sheet2_api)
        response.raise_for_status()
        data = response.json()
        self.customer_data = data["formResponses1"]
        return self.customer_data