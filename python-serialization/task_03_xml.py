#!/usr/bin/python3
"""
Contaim xml method
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    r = ET.Element("root")

    for k, v in dictionary.items():
        child = ET.SubElement(r, k)
        child.text = v

    t = ET.ElementTree(r)

    with open(filename, "wb") as f:
        t.write(f, xml_declaration=True)


def deserialize_from_xml(filename):
    t = ET.parse(filename)
    r = t.getroot()

    d = {}

    for child in r:
        d[child.tag] = child.text
    return d
