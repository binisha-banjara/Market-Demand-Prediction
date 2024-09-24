import requests
import pandas as pd
from datetime import datetime, timedelta


API_KEY = "204241db492f478b8c792655242209"

start_date = datetime(2013, 6, 16)
end_date = datetime(2021, 5, 13)


# Function to fetch data 
def get_weather_data_for_range(start_date, end_date):
    url = f"http://api.worldweatheronline.com/premium/v1/past-weather.ashx"
    payload = {
        "key": API_KEY,
        "q": "Nepal",  
        "format": "json",
        "date": start_date.strftime("%Y-%m-%d"),
        "enddate": end_date.strftime("%Y-%m-%d"),
        "tp": "24",  # Daily weather data
    }

    response = requests.get(url, params=payload)
    if response.status_code == 200:
        data = response.json()["data"]["weather"]
        weather_list = []
        for weather in data:
            weather_list.append(
                {
                    "Date": weather["date"],
                    "Temperature": weather["avgtempC"],
                    "Rainfall": weather["hourly"][0]["precipMM"],
                    "Humidity": weather["hourly"][0]["humidity"],
                }
            )
        return pd.DataFrame(weather_list)
    else:
        print(f"Failed to retrieve data for {start_date} to {end_date}")
        return pd.DataFrame()


def get_weather_data(start_date, end_date):
    delta = timedelta(days=30)  
    all_weather_data = pd.DataFrame()

    current_start = start_date
    while current_start <= end_date:
        current_end = min(current_start + delta, end_date)
        weather_data = get_weather_data_for_range(current_start, current_end)
        all_weather_data = pd.concat(
            [all_weather_data, weather_data], ignore_index=True
        )
        current_start = current_end + timedelta(
            days=1
        )

    return all_weather_data


weather_data = get_weather_data(start_date, end_date)

weather_data.to_csv(
    "weather_data.csv", index=False
) 

print(weather_data)
