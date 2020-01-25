from bs4 import BeautifulSoup
from models.wind import Wind
from models.weather import Weather
from models.tideTime import TideTime
from datetime import datetime as dt


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
    spans = humidity.find_all('span')

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

# endregion

# region Tide Extraction


def extractTides(tideHtml):
    currentTide = __extractCurrentTide(tideHtml)
    return currentTide


def __extractCurrentTide(tideHtml):
    soup = BeautifulSoup(tideHtml, 'html.parser')
    list_items = soup.find_all('li', {'class': ['day', 'current']})
    inner_list_items = []
    for item in list_items:
        if 'Today' in item.text:
            inner_list_items = item.find('ul').find_all('li')

    format = '%I:%M %p'

    tideTimes = []
    for item in inner_list_items:
        tideTimes.append(
            TideTime(dt.strptime(item.find('h3').text, format), item.find('span').text))

    return tideTimes
# endregion
