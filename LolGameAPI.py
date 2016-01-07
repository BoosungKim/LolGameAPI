import json
import urllib.request
import urllib.parse
import pprint
import util.jsonutil as jsonutil

my_api_key = "c647ca86-3442-4cdc-9008-2ff6190863d7"
pp = pprint.PrettyPrinter(indent=4)

# user_name = urllib.parse.quote("Only히야")
# sample_url = "https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/" + user_name + "?api_key=" + my_api_key
# parsed_json = jsonutil.get_json(sample_url)


def get_user_info(user_name):
    user_name = urllib.parse.quote(user_name)
    sample_url = "https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/" + user_name + "?api_key=" + my_api_key
    parsed_json = jsonutil.get_json(sample_url)

    return parsed_json

# pp.pprint(get_user_info("Only히야"))

my_id = 2024142

# game_url = 'https://kr.api.pvp.net/api/lol/kr/v1.3/game/by-summoner/'+str(my_id)+'/recent?api_key=' + my_api_key
# game_json = jsonutil.get_json(game_url)
# print(len(game_json['games']))

# my_champ = [each_game['championId'] for each_game in game_json['games']]
# print(my_champ)
# pp.pprint(game_json['games'])

champ_url = 'http://ddragon.leagueoflegends.com/cdn/5.24.2/data/en_US/champion.json'
champ_json = jsonutil.get_json(champ_url)

for each_champ in champ_json['data'].values():
    pp.pprint(each_champ)
    break