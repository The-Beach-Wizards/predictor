from bs4 import BeautifulSoup
from models.headline import Headline


def prettify(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify


def extractLatestNews(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_h2 = soup.findAll('h2')

    headlines = {}

    for h2 in all_h2:
        if "Latest News" in h2:
            all_li = h2.parent.ul.findAll('li')

            for li in all_li:
                headlines[li.time.text] = Headline(li.a.text, li.a['href'])

    return headlines
