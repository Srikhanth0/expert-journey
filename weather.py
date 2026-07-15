import requests

city = input("Enter a City name:")
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo_data = requests.get(geo_url).json()
if "results" not in geo_data:
    print("Invalid city name")
else:
    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    data = requests.get(url).json()


    for k in data.keys():
        print(k)

    print(data["daily"] )

    dates = data["daily"]["time"]
    max_temps=data["daily"]["temperature_2m_max"]
    min_temps=data["daily"]["temperature_2m_min"]

    for dates, max_temps, min_temps in zip(dates, max_temps, min_temps):
        print(f"On {dates} the maximum temperature is {max_temps} and minimum temperature is {min_temps}")
