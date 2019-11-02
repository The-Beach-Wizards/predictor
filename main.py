import navigator as nav
import extractor as ext

# TODO: Replace with actual call to A-league and build new extractor.
html = nav.getPythonHomepage()
pretty = ext.prettify(html)

headlines = ext.extractLatestNews(html)
