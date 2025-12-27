#!/usr/bin/python3
"""Script that adds CLI arguments to a list and saves it as JSON."""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """Load list from file, add args, and save back to disk."""
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
