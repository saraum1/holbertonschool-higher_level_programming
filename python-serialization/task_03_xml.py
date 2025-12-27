#!/usr/bin/env python3
"""Serialize and deserialize dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into XML and save it to a file.

    Args:
        dictionary (dict): Dictionary to serialize (values stored as text).
        filename (str): Output XML filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = "" if value is None else str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): Input XML filename.

    Returns:
        dict: Dictionary reconstructed from XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = "" if child.text is None else child.text

    return result
