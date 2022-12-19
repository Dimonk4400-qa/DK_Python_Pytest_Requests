import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_response_trainer_name():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id': '1570'})
    assert response.json()['trainer_name'] == 'Dimonk'