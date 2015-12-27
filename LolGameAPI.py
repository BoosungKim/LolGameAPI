import json
import urllib.request
import urllib.parse
import pprint

my_api_key = "c647ca86-3442-4cdc-9008-2ff6190863d7"
user_name = urllib.parse.quote("Only히야")
sample_url = "https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/" + user_name + "?api_key=" + my_api_key

response = urllib.request.urlopen(sample_url)
# print(type(response))

result_bytes = response.read()
# print(type(result_bytes))

result_str = result_bytes.decode('utf-8')
# print(type(result_str))
# print(result_str)

parsed_json = json.loads(result_str)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(parsed_json)
print(type(parsed_json))