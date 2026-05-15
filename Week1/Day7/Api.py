# API stands for "Application Programming Interface." In simple terms, it's a set of rules and protocols that allow how different software applications can communicate and interact with each other. APIs define the methods and data formats that applications can use to request and exchange information. To retrieve data from a web server, a client application initiates a request, and the server responds with the requested data.

# Python-API-Tutorial--1.webp

# n order to work with APIs, some tools are required, such as requests module and we need to first install them in our system.

# Command to install 'requests':

# pip install requests

# Once we have installed it, we need to import it in our code to use it.

# Command to import 'requests':

# import requests

# Let us understand the working of API with examples. First let us take a simple example.

# This example retrieves the latest opening price for IBM stock at a 5-minute interval from alphavantage api endpoint. Here we are using 'requests' to make a call and it is checked with the help of status code that whether our request was successful or not. Then the response is converted to python dictionary and the respected data is stored.

import requests

def get_stock_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        price = data["Time Series (5min)"][last_refreshed]["1. open"]
        return price
    else:
        return None

price = get_stock_data()
symbol = "IBM"
if price is not None:
    print(f"{symbol}: {price}")
else:
    print("Failed to retrieve data.")
    
# Sends a GET request to Alpha Vantage API.
# Checks if the request was successful (status_code == 200).
# Parses JSON response to extract latest opening stock price.
# Prints the price or error message.

# Understanding API Status Codes
# Status codes tell us how the server handled our request:

# 200 OK: Request successful, data returned.
# 201 Created: New resource created.
# 204 No Content: Success but no data returned.
# 400 Bad Request: Invalid request.
# 401 Unauthorized: Missing or invalid API key.
# 500 Internal Server Error: Server encountered an error.
# These codes help in debugging and managing API responses.


import requests

API_KEY = 'c02bb2efaaba48cf873e25b1e2cbd1f8'
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"
respons = requests.get(url)
print(respons.status_code)


# Api key :- c02bb2efaaba48cf873e25b1e2cbd1f8

import json
import requests

def fetch_and_print_articles(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        for index, article in enumerate(articles[:1], start=1):
            print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")
        
        


API_KEY = 'c02bb2efaaba48cf873e25b1e2cbd1f8'
api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}&pageSize=1"

fetch_and_print_articles(api_endpoint)

def jprint(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))
    
    
import requests

API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "c02bb2efaaba48cf873e25b1e2cbd1f8"

params = {
    "country": "us",
    "apiKey": API_KEY,
    "pageSize": 1
}

response = requests.get(API_URL, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    
# Parses JSON from the API response.
# enumerate(articles[:1], start=1) prints details of top 1 news article formatted neatly.
# Handles errors by checking response status.
    
# Example 3: Tracking the International Space Station (ISS) Location
# This example uses several libraries to track ISS in real-time and map its position using Python’s turtle graphics.

# Key libraries used:
# json: For decoding JSON data from API.
# turtle: For graphical map display.
# urllib.request: To fetch API data.
# time: For periodic updates.
# webbrowser: To open files.
# geocoder: To find current user location.

import json
import urllib.request
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "iss.txt")

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

with open(file_path, "w") as file:
    file.write(f"There are currently {result['number']} astronauts on the ISS:\n\n")
    for person in result["people"]:
        file.write(person['name'] + " - onboard\n")
        
import geocoder

g = geocoder.ip('me')
print(f"Your current location: {g.latlng}")  

import json
import urllib.request
import turtle

# Setup the screen
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Uncomment if you have the image files in your directory
screen.bgpic("images/map.gif")
screen.register_shape("images/iss.gif")

# Setup the turtle
iss = turtle.Turtle()
iss.shape("images/iss.gif")
iss.color("red") # Temporary color if the shape image is missing
iss.setheading(45)
iss.penup()

# ISS API endpoint
url = "http://api.open-notify.org/iss-now.json"

def track_iss():
    """Fetches the current ISS location and updates the turtle position."""
    try:
        # Fetch data from the API
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        
        # Extract longitude and latitude
        lat = float(result["iss_position"]["latitude"])
        lon = float(result["iss_position"]["longitude"])
        
        print(f"Current ISS Location: Latitude {lat}, Longitude {lon}")
        
        # Update the turtle's position
        iss.goto(lon, lat)
        
    except Exception as e:
        print(f"Error retrieving data: {e}")
        
    # Call this function again after 5 seconds (5000 milliseconds)
    screen.ontimer(track_iss, 5000)

# Start tracking
track_iss()

# Keep the window open until the user closes it
screen.mainloop()      


# import time
# import urllib.request

# while True:
#     url = "http://api.open-notify.org/iss-now.json"
#     response = urllib.request.urlopen(url)
#     result = json.loads(response.read())

#     lat = float(result["iss_position"]["latitude"])
#     lon = float(result["iss_position"]["longitude"])

#     print(f"Latitude: {lat}, Longitude: {lon}")

#     iss.goto(lon, lat)
#     time.sleep(5)
    
    
import json
import urllib.request
import turtle
import webbrowser
import geocoder

# 1. Fetch current astronauts data
astronauts_url = "http://api.open-notify.org/astros.json"

try:
    with urllib.request.urlopen(astronauts_url) as response:
        astronauts_data = json.loads(response.read())

    # Write astronauts info to a text file
    with open("iss.txt", "w") as file:
        file.write(f"There are currently {astronauts_data['number']} astronauts on the ISS:\n\n")
        for person in astronauts_data["people"]:
            file.write(f"{person['name']} - onboard\n")

        # Get user's current latitude and longitude
        user_location = geocoder.ip('me')
        if user_location.latlng:
            file.write(f"\nYour current lat / long is: {user_location.latlng}")

    # Open the text file in the default web browser
    webbrowser.open("iss.txt")
except Exception as e:
    print(f"Could not retrieve astronaut information: {e}")

# 2. Setup the turtle screen for ISS tracking map
screen = turtle.Screen()
screen.setup(width=1280, height=720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load world map and ISS icon (Make sure files exist or handle gracefully)
try:
    screen.bgpic("images/map.gif")
    screen.register_shape("images/iss.gif")
except FileNotFoundError:
    print("Background image or ISS image missing. Using standard shapes.")

# Create the turtle representing the ISS
iss = turtle.Turtle()
try:
    iss.shape("images/iss.gif")
except:
    iss.shape("turtle") # Fallback to standard turtle shape if image is missing

iss.setheading(45)
iss.penup()

# 3. API endpoint to get ISS current position
iss_position_url = "http://api.open-notify.org/iss-now.json"

def track_iss():
    """Fetches the current position of the ISS and updates the map."""
    try:
        with urllib.request.urlopen(iss_position_url) as response:
            data = json.loads(response.read())

        lat = float(data["iss_position"]["latitude"])
        lon = float(data["iss_position"]["longitude"])

        print(f"Latitude: {lat}, Longitude: {lon}")

        # Update ISS position on the map
        iss.goto(lon, lat)
        
    except Exception as e:
        print(f"Error updating ISS position: {e}")

    # Repeat the function every 5000 milliseconds (5 seconds)
    screen.ontimer(track_iss, 5000)

# Start tracking and run the turtle loop
try:
    track_iss()
    turtle.mainloop()
except KeyboardInterrupt:
    print("\nISS tracking stopped by user.")
    turtle.bye()


# Why Use APIs Instead of Static Data Files?
# Real-time Updates: APIs provide live, constantly updated data (e.g., weather, stock prices).
# Data Size Efficiency: APIs allow fetching only relevant data, unlike downloading large CSV files.
# Specificity: APIs enable targeted queries, minimizing unnecessary data transfer.




