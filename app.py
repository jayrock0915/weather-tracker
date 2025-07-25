import streamlit as st
import requests

# Get the API key from Streamlit secrets
api_key = st.secrets["API_KEY"]

# Streamlit UI
st.title("🌤️ Weather Tracker")
city = st.text_input("Enter city name")

if city:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        st.subheader(f"Weather in {city}")
        st.write(f"**Condition:** {weather}")
        st.write(f"**Temperature:** {temperature} °F")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind_speed} mph")
    else:
        st.error("City not found. Please enter a valid city name.")
# Force update for Streamlit Cloud
