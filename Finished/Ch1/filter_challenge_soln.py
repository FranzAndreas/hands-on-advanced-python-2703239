# Python code​​​​​​‌​‌​​‌‌​​​​‌​​‌​‌‌​​‌‌​​​ below
# Use print("messages...") to debug your solution.
import json

def get_cold_windy_rainy_days():
    # open the sample weather data file and use the json module to load and parse it
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def is_cold_windy_rainy_day(d):
        avg_temp = (d['tmax'] + d['tmin']) / 2
        total_prcp = d['snow'] + d['prcp']
        if avg_temp < 45 and total_prcp > 0.7 and d['awnd'] >= 10.0:
            return True
        return False

    blustery_days = list(filter(is_cold_windy_rainy_day, weatherdata))
    return blustery_days