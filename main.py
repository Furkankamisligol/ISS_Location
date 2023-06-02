import requests
from datetime import datetime

MY_LAT = 0
MY_LNG = 0


def iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    longitude = float(response.json()["iss_position"]["longitude"])
    latitude = float(response.json()["iss_position"]["latitude"])
    if 5 >= longitude - MY_LNG >= -5 and 5 >= latitude - MY_LAT >= -5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    sunset_sunrise = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sunset_sunrise.raise_for_status()
    data = sunset_sunrise.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if not sunrise < time_now < sunset:
        return True


if iss_above() and is_night():
    print("ISS can be seen from your location ")
else:
    print("ISS can't be seen from your location")
