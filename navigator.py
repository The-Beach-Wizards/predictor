import requests


def getWeatherForLocation(location):
    url = "https://www.willyweather.com.au/qld/sunshine-coast/" + location + ".html"
    r = requests.get(url)
    data = r.text
    return data
