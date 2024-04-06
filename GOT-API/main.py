import json
import requests

address = "https://thronesapi.com/api/v2/"

character_key = 'characters'
continents_key = 'continents'

character_required = requests.get(f'{address}{character_key}')
characters = json.loads(character_required.text)

continent_required = requests.get(f'{address}{continents_key}')
continents = json.loads(continent_required.text)


def make_request(complement):
    page = ''
    if complement == "all characters":
        page = "characters"
    elif complement == "all continents":
        page = "continents"

    request = requests.get(f'{address}{page}')
    list_required = json.loads(request.text)

    return list_required


for i in characters:
    for j in i:
        print(j)
