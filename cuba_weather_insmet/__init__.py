__version__ = '0.0.1'

from cuba_weather_municipality import CubaWeatherMunicipality
from .repositories import SourceRepository, WeatherRepository

class CubaWeatherInsMet:
    def __init__(self):
        self._cubaWeatherMunicipality = CubaWeatherMunicipality()
        self._sourceRepository = SourceRepository()
        self._weatherRepository = WeatherRepository()

    def get(self, input: str):
        '''
            Method that given a municipality searches the cuban municipalities to find the best match and returns the weather information.
        '''
        municipality = self._cubaWeatherMunicipality.get(input, suggestion=True)    
        source = self._sourceRepository.getSource(municipality)
        weather = self._weatherRepository.getWeather(source)
        weather.cityName = municipality.name

        return weather