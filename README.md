#Weather Checker CLI – Open-Meteo API Project

This is a Python project that fetches and displays real-time weather information for any city using the [Open-Meteo API](https://open-meteo.com/) and geocoding from the `geopy` library.

The script prompts the user to enter a city name, converts that city to geographic coordinates, makes a call to the Open-Meteo API, and neatly prints the current temperature, wind speed, and timestamp in a formatted table.

---

##Features

- 🔍 Convert any city name into latitude & longitude using `geopy`
- ☁️ Retrieve current weather conditions using Open-Meteo’s free public API
- 🧾 Display the data in a clean CLI table with `tabulate`
- 🔧 Error handling for bad API responses or invalid city names

---

##Example Output

Welcome to Chai's Weather Checker!
Enter city name(e.g. London, Tokyo): Paris
Fetching weather data for Paris (Lat: 48.8534951, Lon: 2.3483915)...
Weather Info        Value
------------------  ----------------
City                Paris
Temperature (°C)    29.5
Wind Speed (km/h)   10.6
Wind Direction (°)  108
Time                2025-07-18T18:30


---

##Requirements

- Python 3.x
- `requests`
- `tabulate`
- `geopy`

Install them using pip:

```bash
pip install requests tabulate geopy
