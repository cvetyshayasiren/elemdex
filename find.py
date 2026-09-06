
import json
import random

from utils import pretty_element

def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def random_element():
    elements = load_data()
    element = random.choice(elements)
    return pretty_element(element)

def element_by_number(number):
    elements = load_data()
    for element in elements:
        if str(element['number']) == number:
            return pretty_element(element)
    return f"no chemical element with this number({number}) was found"

def element_by_name(name):
    elements = load_data()
    for element in elements:
        if element['symbol'].lower() == name.lower():
            return pretty_element(element)

    for element in elements:
        if element['name'].lower() == name.lower():
            return pretty_element(element)

    return f"no chemical element was found for this query ({name})"