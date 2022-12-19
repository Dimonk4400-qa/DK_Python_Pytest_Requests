import requests
import json

token= '7899de870602c97270ea997f73064893'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "name": "Бульбазавр_DK",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": 2506,
    "name": "Бульбазавр_DK1",
    "photo": ""
})

response_add_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token': token}, json={
    "pokemon_id": 2506
})

print(response_add_pokeball.text)
