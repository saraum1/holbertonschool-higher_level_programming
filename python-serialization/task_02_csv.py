#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and write it to data.json.

    Args:
        csv_filename (str): CSV input filename.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as out:
            json.dump(data, out, indent=4)

        return True
    except Exception:
        return False
