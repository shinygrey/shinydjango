import datetime
import requests
import json

class Experiments():
	def __init__(self, userid):
		self.response = requests.get("https://reqres.in/api/users/" + userid)
		self.responsedata = self.response.json()
		self.data = json.loads(self.responsedata)
		
	
	datetime1 = datetime.datetime.now()
