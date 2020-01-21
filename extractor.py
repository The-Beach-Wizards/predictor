from bs4 import BeautifulSoup
from models.wind import Wind


def prettify(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify


def extractCurrentTemperature(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.find('h1')

    return h1.text.strip()[:4]


def extractHumidity(html):
    soup = BeautifulSoup(html, 'html.parser')
    humidity = soup.find('li', {'class': 'humidity'})
    spans = humidity.findAll('span')

    return spans[0].text[:-1]


def extractWind(html):
    soup = BeautifulSoup(html, 'html.parser')
    wind = soup.find('li', {'class': 'wind'})

    direction = wind.find('strong').text

    windAndGustSpeedKmHr = wind.findAll(
        'span')[0].text.strip().replace(' ', '')

    windSpeed = windAndGustSpeedKmHr[:4]
    gustSpeed = windAndGustSpeedKmHr[9:13]

    return Wind(direction, windSpeed, gustSpeed)
