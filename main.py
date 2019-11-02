import navigator as nav
import extractor as ext
import csv


html = nav.getPythonHomepage()
headlines = ext.extractLatestNews(html)

rows = [['Date', 'Headline', 'Link']]

for date, headline in headlines.items():
    row = [date, headline.text, headline.link]
    rows.append(row)

with open('D:\\aleague_data\\headlines.csv', 'w', newline="") as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(rows)

writeFile.close()
