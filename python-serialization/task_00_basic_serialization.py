#!/usr/bin/env python3
"""Basic JSON serialization and deserialization utilities."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to a file.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): Output JSON filename (overwritten if exists).
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it to a dictionary.

    Args:
        filename (str): Input JSON filename.

    Returns:
        dict: Deserialized dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
