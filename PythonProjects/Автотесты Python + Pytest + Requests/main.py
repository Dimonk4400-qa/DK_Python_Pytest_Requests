import requests
import json

response = requests.get('https://pokemonbattle.me:5000/trainers')
response_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(response_json)
