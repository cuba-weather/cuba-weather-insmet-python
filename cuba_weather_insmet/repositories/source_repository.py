from cuba_weather_municipality import MunicipalityModel

class SourceRepository:
  '''
    Class to provide the functionality of searching for a source
  '''

  def getSource(self, municipality: MunicipalityModel):
    '''
      Method that returns the source closest to the given municipality.
    '''
    queryLat = municipality.lat
    queryLon = municipality.lon
    bestSource = sources[0]
    bestDistance = bestSource.distance(queryLat, queryLon)

    for i in range(1, len(sources)):
      tempSource = sources[i]
      tempDistance = tempSource.distance(queryLat, queryLon)

      if tempDistance < bestDistance:
        bestSource = tempSource
        bestDistance = tempDistance

    return bestSource

from math import sqrt

class SourceModel:
  def __init__(self, name: str, lat: float, lon: float):
    self.name = name
    self.lat = lat
    self.lon = lon

  def distance(self, lat: float, lon: float) -> float:
    '''
      Method that return the distance between source and input lat and lon
    '''
    return sqrt(pow(self.lat - lat, 2) + pow(self.lon - lon, 2))

# Sources of weather data
sources = [
  SourceModel(
    name='Pinar del Río',
    lat=22.412222,
    lon=-83.671944,
  ),
  SourceModel(
    name='La Habana',
    lat=23.136667,
    lon=-82.358889,
  ),
  SourceModel(
    name='Varadero',
    lat=23.139444,
    lon=-81.286111,
  ),
  SourceModel(
    name='Cienfuegos',
    lat=22.145556,
    lon=-80.436389,
  ),
  SourceModel(
    name='Cayo Coco',
    lat=22.514722,
    lon=-78.511389,
  ),
  SourceModel(
    name='Camagüey',
    lat=21.383889,
    lon=-77.9075,
  ),
  SourceModel(
    name='Holguín',
    lat=20.886944,
    lon=-76.259167,
  ),
  SourceModel(
    name='Santiago de Cuba',
    lat=20.019833,
    lon=-75.813917,
  ),
]

