# This is a simple weather app in python 
import requests
import json, os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    #print(response.json())
    return response.json()

"""def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    return response.json()"""

def display_weather(data):
    if data.get("cod") == 200:  # Ensure the request was successful
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description.capitalize()}")
    else:
        print("City not found or there was an error retrieving the data. Please enter a valid city name.")


if __name__ == "__main__":
    api_key = os.getenv("WEATHER_API")  # Replace with your actual API key
    while True:
        city_name = input("Enter city name (or 'exit' to quit): ")
        if city_name.lower().strip() == "exit":
            break
        weather_data = get_weather(city_name, api_key)
        display_weather(weather_data)
