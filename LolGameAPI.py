import urllib.request
import json


my_api_key = "c647ca86-3442-4cdc-9008-2ff6190863d7"
sample_url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=" + my_api_key

response = urllib.request.urlopen(sample_url)
print(type(response))

result_bytes = response.read()
print(type(result_bytes))

result_str = result_bytes.decode('utf-8')
print(type(result_str))

obj = json.JSONDecoder.raw_decode(result_str)
print(type(obj))

