# Keep It Simple

from urllib.request import urlopen

locations = [
    ('Pinar del Río', 1),
    ('La Habana', 7),
    ('Varadero', 13),
    ('Cienfuegos', 19),
    ('Cayo Coco', 25),
    ('Camagüey', 31),
    ('Holguín', 37),
    ('Santiago de Cuba', 43)
]

def get_forecast():
    url = 'http://www.insmet.cu/asp/genesis.asp?TB0=PLANTILLAS&TB1=PT5'

    res = urlopen(url)

    content = str(res.read())

    fecha = content[content.find('fecha5'):content.find(';  //fecha del pronostico para 5 dias')]
    fecha = fecha.split('=')[1].replace('"', '')

    content = content[content.find('pdia'):content.find('ndia')]
    content = content[content.find('(')+1:content.find(')')]
    content = content.replace("\\'", '')

    adata = content.split(',')

    data = dict()

    for l in locations:
        data[l[0]] = []

        d = 1

        for i in range(l[1], l[1]+5):
            data[l[0]].append(WeatherDayModel(d, adata[i]))
            d += 1

    return WeatherJSONModel(fecha, data)

class WeatherJSONModel():
    def __init__(self, date, data):
        self.date = date
        self.data = data

    def __str__(self):
        result = ''

        result += 'Date: {}\n'.format(self.date)

        for l in locations:
            result += '{}:\n'.format(l[0])

            for day in self.data[l[0]]:
                result += str(day)

            result += '\n'

        return result


class WeatherDayModel():
    def __init__(self, day, data: str):
        self.day = day

        temps = data[0:5]

        self.tmax, self.tmin = temps.split(' ')

        self.description = data[6:]

    def __str__(self):
        return '''
            Day: {}, 
            Maximum Temperature: {}°C, 
            Minimum Temperature: {}°C, 
            Description: {}
        '''.format(self.day, self.tmax, self.tmin, self.description)