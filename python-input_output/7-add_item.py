#!/usr/bin/python3


'''Module Doc'''


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file


arguments = sys.argv
data = []
filename = "add_item.json"

try:
    existing_data = load_from_json_file(filename)
    data.extend(existing_data)
except FileNotFoundError:
    pass

for i in range(1, len(arguments)):
    data.append(arguments[i])

save_to_json_file(data, filename)
