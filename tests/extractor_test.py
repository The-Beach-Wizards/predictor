import extractor


def test_extractLatestNews():
    with open("C:\\devel\\python\\aleague\\tests\\python_latestnews.html") as file:
        data = file.read()
        headlines = extractor.extractLatestNews(data)
        dates = list(headlines.keys())

        assert len(dates) == 5

        assert dates[0] == '2019-10-31'
        assert headlines[dates[0]
                         ].text == 'The 2019 Python Developer Survey is here, take a few minutes to complete the survey!'
        assert headlines[dates[0]
                         ].link == 'http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/Y4CDqUEnEB8/the-2019-python-developer-survey-is.html'

        assert dates[4] == '2019-10-19'
        assert headlines[dates[4]].text == 'Python 2.7.17 released'
        assert headlines[dates[4]
                         ].link == 'http://feedproxy.google.com/~r/PythonInsider/~3/NSJOxfu3Kw0/python-2717-released.html'

    file.close()
