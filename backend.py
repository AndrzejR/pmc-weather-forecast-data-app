import os
import requests


def get_weather_data(place, days, kind="Temperature"):
    city_id = place  # lookup from file
    api_key = os.environ['PMC_OWMAP_API_KEY']
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_id}&appid={api_key}&units=metric&lang=en"
    response = requests.get(url)

    x, y = [], []
    if response.status_code == 200:
        data = response.json()
        data_list = data['list'][:days * 8]
        x = [r['dt_txt'] for r in data_list]
        if kind == "Temperature":
            y = [r['main']['temp'] for r in data_list]
        if kind == "Sky":
            y = [r['weather'][0]['main'] for r in data_list]
    return x, y


if __name__ == "__main__":
    print(get_weather_data("Warsaw", 5, "temperature"))
