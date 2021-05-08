import requests
import json

number = input("Please enter a pokemon number: ")
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/3{number}")

pokemon = response.json()
print(pokemon['name'].upper())