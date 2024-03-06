#!/usr/bin/python3
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
A script that adds all arguments to a Python list,
and then save them to a file
"""
if __name__ == "__main__":
    args = sys.argv[1:]
    existing_list = load_from_json_file("add_item.json")
    existing_list.extend(args)
    save_to_json_file(existing_list, "add_item.json")
