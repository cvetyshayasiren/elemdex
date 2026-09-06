import re
import shutil
import textwrap

def electron(element: dict):
    el_conf = element["electron_configuration"].split()
    el_conf_dict = {item: int(item[2:]) for item in el_conf}
    output = ""

    for k, v in el_conf_dict.items():
        spaces = " " * (5 - len(k))
        output += f"\n{k}{spaces}|{v * "*"}"
    return(output.strip())


def color_text(text, color = 'purple'):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}\033[0m"


def clean_len(text):
    return len(text) - len(re.sub(r'\033\[[0-9;]*m', '', text))


def category(element: dict):
  return color_text(element['category'])


def frame(text: str, margin: int = 1):
    width = shutil.get_terminal_size().columns

    lines = []
    for line in text.split('\n'):
        lines.extend(textwrap.wrap(line, width - margin * 2 - 2) or [''])

    border_up = "┌" + "─" * (width - 2) + "┐"
    border_down = "└" + "─" * (width - 2) + "┘"
    result = [border_up]
    for line in lines:
        string = "│" + " " * margin + line.ljust(width - margin - 2)
        clean = f"{clean_len(string) * ' '}│"
        result.append(string + clean)

    result.append(border_down)
    return "\n".join(result)


def pretty_element(element: dict):
    output = []

    head = f"{element['symbol']} {element['number']} {element['name'].upper()} │ {category(element)}"
    body = f"{element["appearance"]}\natomic mass {color_text(element['atomic_mass'], "red")}\nboil {element['boil']} │ melt {element['melt']}\ndensity {element['density']}"
    body2 = f"discovered by {color_text(element['discovered_by'], "green")}\nphase {element['phase']}\nperiod {element['period']} │ group {element['group']}"
    body3 = f"{element['source']}\n{element['summary']}"
    body4 = electron(element)

    output.append(frame(head))
    output.append(frame(body))
    output.append(frame(body2))
    output.append(frame(body3))
    output.append(frame(body4))
    return "\n".join(output)