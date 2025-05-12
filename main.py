import requests
from twilio.rest import Client
import os

# --- Environment Variables ---
# These should be set in your environment (e.g., via a .env file or system config)
api_key = os.getenv("OWM_API_KEY")             # OpenWeatherMap API Key
account_sid = os.getenv("TWILIO_ACCOUNT_SID")  # Twilio Account SID
auth_token = os.getenv("TWILIO_AUTH_TOKEN")    # Twilio Auth Token
from_phone = os.getenv("TWILIO_PHONE")         # Twilio SMS phone number (e.g., "+1XXXXXXXXX")
to_phone = os.getenv("MY_PHONE_NUMBER")        # Your phone number
from_whatsapp = os.getenv("TWILIO_WA_FROM")    # Twilio WhatsApp sender (e.g., "whatsapp:+1XXXXXXXXXX")
to_whatsapp = os.getenv("MY_WA_NUMBER")        # Your WhatsApp number

# --- Location Coordinates (Ahmedabad, India) ---
MY_LAT = 23.022505
MY_LONG = 72.571365

# --- Get Weather Forecast Data ---
response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LONG}&appid={api_key}"
)
response.raise_for_status()
weather_data = response.json()

# --- Check for Rain in Forecast ---
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
        break

# --- Send Notification via Twilio ---
client = Client(account_sid, auth_token)

if will_rain:
    print("Bring an umbrella ☔")
    message = client.messages.create(
        body="It's going to rain today! ☔",
        from_=from_phone,
        to=to_phone
    )
    message_wp = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_=from_whatsapp,
        to=to_whatsapp
    )
else:
    print("Don't bring an umbrella ☀️")
    message = client.messages.create(
        body="It's not going to rain today!",
        from_=from_phone,
        to=to_phone
    )
    message_wp = client.messages.create(
        body="It's not going to rain today ☀️",
        from_=from_whatsapp,
        to=to_whatsapp
    )

print("SMS status:", message.status)
