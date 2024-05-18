import json
import requests

address = "https://thronesapi.com/api/v2/"

character_key = 'characters'
continents_key = 'continents'

character_required = requests.get(f'{address}{character_key}')
characters = json.loads(character_required.text)

continent_required = requests.get(f'{address}{continents_key}')
continents = json.loads(continent_required.text)


families = dict()
for i in characters:
    unknown = ['Unknown', 'None', 'Unkown', '']
    for j in i:
        if j == 'family':
            if i[j][:5] == 'House':
                families[i[j][6:]] = list()
            elif i[j] in unknown:
                families['Unknown'] = list()
            else:
                families[i[j]] = list()

for i in characters:
    unknown = ['Unknown', 'None', 'Unkown', '']
    for j in i:
        if j == 'family':
            if i[j][:5] == 'House':
                families[i[j][6:]].append((i['fullName'], i['id']))
            elif i[j] in unknown:
                families['Unknown'].append((i['fullName'], i['id']))
            else:
                families[i[j]].append((i['fullName'], i['id']))


for i in families:
    print(i)
    print(families[i])

