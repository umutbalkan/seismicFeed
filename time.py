class Time:
	def __init__(self, hour, minute, second):
		self.hour = hour
		self.minute = minute
		self.second = second


	def __str__(self):
		stats = hour + ":" + minute + ":" + second
		return stats