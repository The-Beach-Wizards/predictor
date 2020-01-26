import navigator as nav
import extractor as ext
import csv


weatherHtml = nav.getWeatherForLocation('mount-coolum')
weather = ext.extractWeather(weatherHtml)

print("Temperature: " + weather.temperature + " C")
print("Humidity: " + weather.humidity + " %")
print("Wind speed: " + weather.wind.strength + "km/hr " +
      weather.wind.direction + " (" + weather.wind.gusts + " km/hr Gusts)")

tideHtml = nav.getTidesForLocation('mount-coolum')
currentTideInformation = ext.extractTides(tideHtml)

print('Current tide: ' + str(currentTideInformation.currentTide))
print('Movement direction: ' + currentTideInformation.movement)

# TODO: Replace this with new database entries for weather.
# rows = [['Date', 'Headline', 'Link']]
# for date, headline in headlines.items():
#     row = [date, headline.text, headline.link]
#     rows.append(row)
# with open('C:\\headlines.csv', 'w', newline="") as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(rows)
# writeFile.close()
