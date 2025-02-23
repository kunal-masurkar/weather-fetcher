import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
        }
        return weather
    else:
        return None

if __name__ == "__main__":
    API_KEY = "place your api key here"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_data = get_weather(city, API_KEY)
    
    if weather_data:
        print(f"\nWeather in {weather_data['city']}:\n")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Condition: {weather_data['weather']}")
    else:
        print("Error fetching weather data. Check city name or API key.")
