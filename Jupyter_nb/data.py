import json
import os

with open('dummy.json') as d:
    names = json.load(d)
    data = names.get('firstNames', [])