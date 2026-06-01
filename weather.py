import requests
import json
from datetime import datetime

CITIES = {
    "Dubai": {"lat": 25.20, "lon": 55.27},
    "Abu Dhabi": {"lat": 24.45, "lon": 54.38},
    "Sharjah": {"lat": 25.35, "lon": 55.39},
}

def get_weather(lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m,relative_humidity_2m",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {}

def collect_all_cities(cities: dict) -> list:
    results = []
    for city_name, coords in cities.items():
        print(f"Request the weather: {city_name}...")
        data = get_weather(coords["lat"], coords["lon"])
        
        if data:
            current = data["current"]
            results.append({
                "city": city_name,
                "temperature": current["temperature_2m"],
                "humidity": current["relative_humidity_2m"],
                "wind_speed": current["wind_speed_10m"],
                "timestamp": datetime.now().isoformat(),
            })
    return results

def save_to_json(data: list, filename: str) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"Saved to {filename}")
    except OSError as e:
        print(f"Saving error: {e}")

def find_hottest_city(data: list) -> dict:
    hottest_city = max(data, key=lambda city: city['temperature'])
    return hottest_city

def main():
    print("=== Weather Collector ===\n")
    weather_data = collect_all_cities(CITIES)
    if weather_data:
        print("\n=== Results ===")
        for record in weather_data:
            print(f"{record['city']}: {record['temperature']}°C, "
                f"humidity {record['humidity']}%, "
                f"wind {record['wind_speed']} km/h")
        
        print(f"\nThe hottest city: {find_hottest_city(weather_data)['city']}")
        save_to_json(weather_data, "weather_data.json")


if __name__ == "__main__":
    main()