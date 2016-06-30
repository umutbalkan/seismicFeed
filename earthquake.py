from date import Date
from time import Time
from coordinates import Coordinates
from location import Location
from bs4 import BeautifulSoup

class Earthquake:
	def __init__(self, year, month, day, h, min, sec, lat, long , magnitude, loc):
		self.date = Date(year, month, day)
		self.time = Time(h, min, sec)
		self.coordinates = Coordinates(lat, long)
		self.magnitude = magnitude
		self.location = Location(loc)