from ..insmet_webparser import get_forecast

class WeatherRepository:
  '''
    Class to provide the functionality of obtaining weather data
  '''
  def __init__(self):
    self.weatherdata = get_forecast()

  def getWeather(self, source):
    return WeatherModel(
      date = self.weatherdata.date, 
      cityName=source.name,
      data=self.weatherdata.data[source.name]
    )

class WeatherModel():
  def __init__(self, date, cityName, data):
    self.date = date
    self.cityName = cityName
    self.days = data

  def __str__(self):
    result: str = ''
    result += 'City Name: {}\n'.format(self.cityName)
    result += 'Datetime Update: {}\n'.format(self.date)

    for i in range(0, len(self.days)):
      result += '{}\n'.format(self.days[i])

    #result += 'Today\'s Weather Forecast: ${}\n'.format(self.weatherForecast)
    #result += 'Drought Status: {}'.format(self.droughtStatus)
    
    return result