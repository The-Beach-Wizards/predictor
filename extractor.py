from bs4 import BeautifulSoup
from models.wind import Wind
from models.weather import Weather


def prettify(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify


# region Weather Extraction


def extractWeather(weatherHtml):
    currentTemperature = __extractCurrentTemperature(weatherHtml)
    humidity = __extractHumidity(weatherHtml)
    wind = __extractWind(weatherHtml)

    return Weather(currentTemperature, humidity, wind)


def __extractCurrentTemperature(html) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.find('h1')

    return h1.text.strip()[:4]


def __extractHumidity(html) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    humidity = soup.find('li', {'class': 'humidity'})
    spans = humidity.findAll('span')

    return spans[0].text[:-1]


def __extractWind(html) -> Wind:
    soup = BeautifulSoup(html, 'html.parser')
    wind = soup.find('li', {'class': 'wind'})

    direction = wind.find('strong').text

    windAndGustSpeedKmHr = wind.findAll(
        'span')[0].text.strip().replace(' ', '')

    windSpeed = windAndGustSpeedKmHr[:4]
    gustSpeed = windAndGustSpeedKmHr[9:13]

    return Wind(direction, windSpeed, gustSpeed)
