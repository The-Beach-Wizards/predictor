from models.wind import Wind


class Weather:
    def __init__(self, temperature: str, humidity: str, wind: Wind):
        self.temperature = temperature
        self.humidity = humidity
        self.wind = wind
