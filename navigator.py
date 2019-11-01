import requests


def getPythonHomepage():
    url = "https://www.python.org/"
    r = requests.get(url)
    data = r.text
    return data
