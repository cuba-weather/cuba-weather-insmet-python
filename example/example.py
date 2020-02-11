from cuba_weather_insmet import CubaWeatherInsMet

api = CubaWeatherInsMet()

weather = api.get('Santiago')

print(weather)
