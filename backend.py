import requests

API_KEY = "51d5a0146d572195bc15749d93d44c4e"
def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(data)
    filtered_data = data["list"]
    filtered_data = filtered_data[:8*forecast_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Baku", forecast_days=3))


