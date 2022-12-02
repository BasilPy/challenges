import requests
import os
from twilio.rest import Client

sid =  os.environ.get("TWILIO_ACCOUNT_SID")
token = os.environ.get("TWILIO_AUTH_TOKEN")
API_key =os.environ.get("API_KEY")
lat = 43.2220
lon = 76.8512

parameters = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "appid": API_key
}

# resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Almaty,KZ&appid={API_key}")
# resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}")
resp = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
resp.raise_for_status()
weather_data = resp.json()
# print(weather_data['weather'][0])
# print(weather_data)
# weather_hour0 = weather_data["hourly"][0]["weather"][0]["id"]
# print(weather_hour0)
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        # print("take your umbrella!")
if will_rain:
    print("take your umbrella!")
else:
    print("probability of raining is low")
# Download the helper library from https://www.twilio.com/docs/python/install


# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure

# client = Client(sid, token)

# message = client.messages.create(
#     body="Good morning! Have a great day!",
#     from_="+",
#     to="+"
# )

# print(message.sid)