import json
import random
import sys

from utils import pretty_element

def main():

    if len(sys.argv) != 2:
        print("-p ")
        sys.exit(1)

    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print(sys.argv[0])


    element = random.choice(data)
    # print(pretty_element(element))


main()