#! /usr/bin/env python3

import json

output_file = open('input.txt', 'w')

with open('comments2.json', 'r') as json_data:
    data = json.load(json_data)
    for c in data['comments']:
        output_file.write('%s\n'%c['commentText'])

output_file.close()