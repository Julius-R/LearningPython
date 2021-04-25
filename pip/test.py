# Download pip packages with pip install package name
# uninstall with pip uninstall pkg name

import camelcase
import requests

c = camelcase.CamelCase()
r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

data = dict(r.json())
print(c.hump(data.get('name')))