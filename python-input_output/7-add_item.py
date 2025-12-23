#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to add_item.json."""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """Load list, extend with args, and save back to add_item.json."""
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
