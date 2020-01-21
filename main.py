import navigator as nav
import extractor as ext
import csv


html = nav.getWeatherForLocation('mount-coolum')
currentTemperature = ext.extractCurrentTemperature(html)
humidity = ext.extractHumidity(html)
wind = ext.extractWind(html)

print("Temperature: " + currentTemperature + " C")
print("Humidity: " + humidity + " %")
print("Wind speed: " + wind.strength + "km/hr " +
      wind.direction + " (" + wind.gusts + " km/hr Gusts)")

# TODO: Replace this with new database entries for weather.
# rows = [['Date', 'Headline', 'Link']]
# for date, headline in headlines.items():
#     row = [date, headline.text, headline.link]
#     rows.append(row)
# with open('C:\\headlines.csv', 'w', newline="") as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(rows)
# writeFile.close()
