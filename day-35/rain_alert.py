from secrets import OPEN_WEATHER_API_KEY, \
    TWILIO_AUTH_TOKEN, \
    TWILIO_ACCOUNT_SID, \
    TWILIO_PHONE_NUMBER, \
    MY_PHONE_NUMBER, \
    MY_LAT, \
    MY_LON
import requests
from twilio.rest import Client

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'exclude': 'current,minutely,daily',
    'appid': OPEN_WEATHER_API_KEY
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

# for i in range(0, 12):
#     weather_id = weather_data['hourly'][i]['weather'][0]['id']
#     if weather_id < 700:
#         print(f"Bring Umbrella at {i+1}")

will_rain = False
weather_slice = weather_data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='It is going to rain today, remember to bring an ☔️',
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )
    print(message.status)