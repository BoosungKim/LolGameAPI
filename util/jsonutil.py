import json
import urllib.request


def get_json(url):
    return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))