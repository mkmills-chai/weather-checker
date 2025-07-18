import requests
from tabulate import tabulate
from geopy.geocoders import Nominatim

#Get city input from user
print("Welcome to Chai's Weather Checker!")
city = input("Enter city name(e.g. London, Tokyo): ")

#Convert city name to coordinates
geolocator = Nominatim(user_agent="weather_checker")
location = geolocator.geocode(city)

if not location:
    print("City not found. Please check the city name and try again.")
    exit()
    
lat,lon = location.latitude, location.longitude
print(f"Fetching weather data for {city} (Lat: {lat}, Lon: {lon})...")

#Build API URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()['current_weather']
    
    table = [
        ["City", city.title()],
        ["Temperature (°C)", data['temperature']],
        ["Wind Speed (km/h)", data['windspeed']],
        ["Wind Direction (°)", data['winddirection']],
        ["Time", data['time']]
    ]
    print(tabulate(table, headers=["Weather Info", "Value"]))
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
    exit()