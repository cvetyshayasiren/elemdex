import argparse

from find import element_by_name, element_by_number, random_element

def main():
    parser = argparse.ArgumentParser(description= "Program for working with chemical elements")

    parser.add_argument('-r', '--random', action='store_true', help='Return a random element')
    parser.add_argument('element', nargs='?', default=None, help='Element name or number')
    args = parser.parse_args()

    if args.random or args.element is None:
        print(random_element()); return

    element_input = args.element

    if element_input.isdigit():
        print(element_by_number(element_input)); return 
    else:
        print(element_by_name(element_input)); return
    


if __name__ == "__main__":
    main()