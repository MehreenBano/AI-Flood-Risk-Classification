import requests


def get_flood_risk(latitude, longitude):
    api_url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,precipitation,rain",
    }

    response = requests.get(api_url, params=params)

    if response.status_code != 200:
        print("API request failed.")
        print("Status code:", response.status_code)
        return

    data = response.json()
    current = data["current"]

    temperature = current["temperature_2m"]
    precipitation = current["precipitation"]
    rain = current["rain"]

    if precipitation >= 10 or rain >= 10:
        risk = "High"
    elif precipitation >= 2 or rain >= 2:
        risk = "Medium"
    else:
        risk = "Low"

    print("\n--- Flood Risk Assessment ---")
    print("Temperature:", temperature, "°C")
    print("Precipitation:", precipitation, "mm")
    print("Rain:", rain, "mm")
    print("Flood Risk:", risk)


print("AI Flood Risk Classification")
print("----------------------------")

try:
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    get_flood_risk(latitude, longitude)

except ValueError:
    print("Please enter valid numbers for latitude and longitude.")