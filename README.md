# ☔ RainAlert – Smart Weather Notification System

**RainAlert** is a Python-based weather monitoring tool that notifies you via **SMS** and **WhatsApp** if it's going to rain in your area. It uses the **OpenWeatherMap API** for real-time weather forecasts and **Twilio** to send alerts right to your phone.

---

## 🚀 Features

- 🌦️ Real-time 5-day/hourly weather forecast
- 📲 Sends an **SMS alert** if rain is expected
- 💬 Sends a **WhatsApp alert** with the same message
- 🔁 Automatically differentiates between "rainy" and "clear" forecasts
- 🔒 Secure API credentials using a `.env` file

---

## 📸 Screenshots

### ✅ WhatsApp Alert (Rain Forecast)

![WhatsApp Rain Alert](![image](https://github.com/user-attachments/assets/682a21c5-3c6c-4f2e-8f9b-7f81cfd2e200)
)

### ✅ SMS Alert (Rain Forecast)

![SMS Rain Alert](![WhatsApp Image 2025-05-12 at 18 00 46_ce020fce](https://github.com/user-attachments/assets/785560e9-4ad0-45e0-b2d4-80de5baaf33c)
)

> 🔁 You can customize these messages or localize them as needed.

---

## 📦 Tech Stack

- [Python](https://www.python.org/)
- [OpenWeatherMap API](https://openweathermap.org/forecast5)
- [Twilio Messaging API](https://www.twilio.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/rainalert.git
cd rainalert
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a .env file in the root directory with your API keys and phone numbers:

```
# OpenWeatherMap
OWM_API_KEY=your_openweathermap_api_key

# Twilio
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE=+1234567890
MY_PHONE_NUMBER=+919xxxxxxxxx
TWILIO_WA_FROM=whatsapp:+14155238886
MY_WA_NUMBER=whatsapp:+919xxxxxxxxx
```

## 📤 How It Works
Fetches hourly forecast using OpenWeatherMap.

Checks for weather condition codes < 700 (indicating precipitation).

If rain is predicted:

      ✅ SMS: “It's going to rain today! ☔”

      ✅ WhatsApp: “It's going to rain today. Bring an umbrella ☔”

If clear:

      ✅ SMS: “It's not going to rain today ☀️”

      ✅ WhatsApp: “Enjoy your day, no rain expected ☀️”
## Run the Script
```
python rain_alert.py
```
## 🧠 Future Enhancements
Email alerts via SMTP

Schedule daily check with cron job

Add UI dashboard for weather reports

Push alerts to Telegram or Slack
