import datetime
import requests
import json

class Xkcd():
	def __init__(self, comic):
		self.response = requests.get("https://xkcd.com/" + str(comic) + "/info.0.json")
		self.data = self.response.json()


class Experiments():
	def __init__(self, userid):
		self.response = requests.get("https://reqres.in/api/users/" + userid)
		self.data = self.response.json()
		
	
	datetime1 = datetime.datetime.now()
