import json
import urllib.request
import urllib.parse
import pprint
import util.jsonutil as jsonutil
import util.dbutil as dbutil

my_api_key = "c647ca86-3442-4cdc-9008-2ff6190863d7"
pp = pprint.PrettyPrinter(indent=4)


def get_user_info(user_name):
    """
    {'only히야': {'profileIconId': 7, 'revisionDate': 1451794875000, 'summonerLevel': 30, 'id': 2024142, 'name': 'Only히야'}}
    """
    user_name = urllib.parse.quote(user_name)   # url encoding
    sample_url = ("https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/{0}?"
                  "api_key={1}"
                  ).format(user_name, my_api_key)
    parsed_json = jsonutil.get_json(sample_url)

    return parsed_json


def get_user_id(user_name):
    """
    Return user's id(integer)
    """
    default_id = 0
    user_info = get_user_info(user_name)[user_name]
    if user_info:
        default_id = user_info.get('id', default_id)

    return default_id


def get_recent_games(user_name, n=10):
    """
    {'championId' : , 'createDate' : , 'fellowPlayers' : , 'gameId' : ......}
    """
    userid = get_user_id(user_name)
    game_url = ('https://kr.api.pvp.net/api/lol/kr/v1.3/game/by-summoner/{0}/recent?'
                'api_key={1}'
                ).format(userid, my_api_key)

    game_json = jsonutil.get_json(game_url)

    # my_champ = [each_game['championId'] for each_game in game_json['games']]
    # print(my_champ)
    return game_json['games'][0:n]


def champ_info_to_db():
    """
    Get champion information from web and store it to my db
    """
    champ_json = jsonutil.get_json('http://ddragon.leagueoflegends.com/cdn/5.24.2/data/en_US/champion.json')

    for each_champ in champ_json['data'].values():
        d = {}
        for key in ['key', 'name', 'title']:
            d[key] = each_champ[key]

        dbutil.insert_record(d)


# 챔프 아이디로 챔프 이름을 가지고 오려고 하는데, 매 번 DB 에 접근하는거보다는 메모리로 읽어서 하는게 더 좋을 듯
# 메모리로 가지고 올 때 어떤 방식으로 가지고 올까

if __name__ == '__main__':
    pp.pprint(get_recent_games('only히야', 1))
    pass
