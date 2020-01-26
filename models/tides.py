from models.tideTime import TideTime
from typing import List


class Tides:
    def __init__(self, currentTide: str, movement: str, tideTimes: List[TideTime]):
        self.currentTide = currentTide
        self.movement = movement
        self.tideTimes = tideTimes
