class Coordinates:
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	#Accessors
	def getLatitude(self):
		return latitude

	def getLongitude(self):
		return longitude

	def __str__(self):
		stats = "Latitude(N) = " + latitude + "\tLongitude(E) = " + longitude;