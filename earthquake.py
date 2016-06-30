from date import Date
#from time import Time
from coordinates import Coordinates
from location import Location
from bs4 import BeautifulSoup
import requests
import time

class Earthquake:
	def __init__(self, year, month, day, h, min, sec, lat, long , magnitude, loc):
		self.date = Date(year, month, day)
		#self.time = Time(h, min, sec)
		self.coordinates = Coordinates(lat, long)
		self.magnitude = magnitude
		self.location = Location(loc)


def start(url):
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code, "html.parser")


	# Extracts all locations and modifies them
	locs_raw = soup.find_all(style="font-size:10")
	for locs in locs_raw:
		location = locs.string
		#print(type(location))
		str(location)
		length = len(location)
		if "(REVIZE" in location: # removing unmeaningful text
			location = location[0:length-15]
			length -= 15
		if "  " in location: # removing unnecessary blank spaces
			location = location[0:length-4]
			length -= 4
		#print(length,"\t",location)

	date_raw = soup.find_all("td", width="80")
	for dates in date_raw:
		date = dates.string
		#print (date)

	time_raw = soup.find_all("td", width="64",)
	for times in time_raw[1:]: # first element is irrevelant
		time = times.string
		print(time)
start("http://www.kandilli.info/")