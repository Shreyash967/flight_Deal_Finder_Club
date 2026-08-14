> Built under the guidance of Dr. Angela Yu from the 100 Days of Code Bootcamp on Udemy.

# Flight Deal Finder & Notifier

## Description

This project is an automated flight search and notification system. It utilizes the SerpApi Google Flights API to find the cheapest flights from London Heathrow (LHR) to various destinations over a six-month period. 
The system retrieves target destinations and desired price thresholds stored in a Google Sheet via the Sheety API. 
If a flight is found that meets the criteria, it automatically emails all subscribed customers with the cheapest flight details.

## Features

* Connects to Google Sheets using the Sheety API to retrieve destination data, target prices, and a list of subscriber emails.


* Searches for both direct and indirect flights using the SerpApi flight engine.


* Parses flight data to extract the lowest price, origin airport, destination airport, departure date, and number of stops.


* Implements the `requests_cache` module to cache API responses and reduce redundant network calls.


* Sends automated email alerts to users via `smtplib` and a Gmail account when a low price is detected.


* Secures sensitive data such as API keys, email addresses, and passwords using environment variables with the `dotenv` library.



## Output / Usage

* Requires a `.env` file containing the necessary API keys and credentials (`sheety_api1`, `sheet2_api`, `serpapi`, `gmail`, `password`).


* When executed, the script prints the flight search progress, checking each destination and outputting the lowest found prices in the console.


* If no direct flights are available, the system automatically searches for indirect flights and logs the cheapest option.


* Subscribers receive an email structured as: "Low price alert! Only GBP [Price] to fly from [Origin] to [Destination], on [Date] with [Stops] stop(s).".
