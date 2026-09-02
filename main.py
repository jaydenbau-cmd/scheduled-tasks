import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
parameters = {
    "lat": -26.1417,
    "lon": 27.9350,
    "appid": api_key,
    "cnt": 4,
}

codes_list = []

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
index = 0

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

    codes_list.append(condition_code)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+27645143035",
        from_="+17372508034",
        body="sms_event_notifications",
    )
    print(message.status)

