#!/usr/bin/python3
"""Load, add, save

A script that adds all arguments to a Python list,
and then saves the list to a file:

It uses the function save_to_json_file defined in 5-save_to_json_file.py
And the function load_from_json_file defined in 6-load_from_json_file.py
The list is saved as a JSON representation in a file named add_item.json
The file is created if it doesn’t exist
File permissions / exceptions are not managed

"""
import sys
import json
filename = "add_item.json"
"""str: File to load and save to"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""function: To save object to a file"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""function: To Create object from a JSON file"""

empty_file = 0
"""int: To check if the the file has contents"""
with open(filename, "a+", encoding="utf-8") as f:
    f.seek(0)
    contents = f.read()
    if not contents:
        empty_file = 1
if empty_file == 1:
    save_to_json_file(sys.argv[1:], filename)
else:
    new_list = load_from_json_file(filename)
    new_list += sys.argv[1:]
    """list: Stores list from file and list from command line arguments"""
    save_to_json_file(new_list, filename)
