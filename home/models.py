import datetime
import requests
import json

class Experiments():
	def __init__(self, userid):
		self.response = requests.get("https://reqres.in/api/users/" + userid)
		self.data = self.response.json()
		
	
	datetime1 = datetime.datetime.now()
