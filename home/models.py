import datetime
import requests

class Experiments():
	def __init__(self):
		self.response = requests.get("https://reqres.in/api/users/2")
		
	responsedata = response.json()
	datetime1 = datetime.datetime.now()
