# ⚛️ ElemDex

> A lightweight command-line tool for exploring chemical elements

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📖 Description

**ElemDex** is a simple yet powerful CLI utility that allows you to quickly retrieve information about chemical elements directly from your terminal. Whether you're a student, researcher, or just curious about chemistry, ElemDex makes element lookup fast and convenient.

---

## ✨ Features

- 🔍 **Look up elements** by name or atomic number
- 🎲 **Random element** — discover something new with the `--random` flag
- 📋 **Clear, formatted output** with essential element data
- ⚡ **Lightweight and fast** — no dependencies required

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/cvetyshayasiren/elemdex.git
cd elemdex

# Install the package
pip install .
```

---

## 🎯 Usage

### Basic Syntax

```bash
python elemdex.py [OPTIONS] [ELEMENT]
```

### Examples

#### Look up an element by name
```bash
python elemdex.py Hydrogen
```

#### Look up an element by atomic number
```bash
python elemdex.py 79
```

#### Get a random element
```bash
python elemdex.py --random
# or
python elemdex.py -r
```

#### Display help
```bash
python elemdex.py --help
```

---

## 📊 Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-r, --random` | Return a random element |

---

## 📝 Arguments

| Argument | Description |
|----------|-------------|
| `element` | Element name (e.g., "Oxygen") or atomic number (e.g., 8) |

---

## 🖥️ Example Output

```
$ elemdex.py Carbon
┌──────────────────────────────────────────────────────────────────────────────────┐
│ C 6 CARBON │ polyatomic nonmetal                                                 │
└──────────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────────┐
│ None                                                                             │
│ atomic mass 12.011                                                               │
│ boil None │ melt None                                                            │
│ density 1.821                                                                    │
└──────────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────────┐
│ discovered by Ancient Egypt                                                      │
│ phase Solid                                                                      │
│ period 2 │ group 14                                                              │
└──────────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────────┐
│ https://en.wikipedia.org/wiki/Carbon                                             │
│ Carbon (from Latin:carbo "coal") is a chemical element with symbol C and atomic  │
│ number 6. On the periodic table, it is the first (row 2) of six elements in      │
│ column (group) 14, which have in common the composition of their outer electron  │
│ shell. It is nonmetallic and tetravalent—making four electrons available to form │
│ covalent chemical bonds.                                                         │
└──────────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 1s2  |**                                                                         │
│ 2s2  |**                                                                         │
│ 2p2  |**                                                                         │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Requirements

- Python 3.6 or higher

---

## 📦 Project Structure

```
elemdex/
├── elemdex.py      # Main executable
├── README.md       # This file
└── LICENSE         # MIT License
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Data sourced from [periodic table datasets](https://github.com/Bowserinator/Periodic-Table-JSON)
- Built with ❤️ for the chemistry community

---

## 📬 Contact

**Author:** cvetyshayasiren  
**GitHub:** [@cvetyshayasiren](https://github.com/cvetyshayasiren)  
**Project Link:** [https://github.com/cvetyshayasiren/elemdex](https://github.com/cvetyshayasiren/elemdex)

---

*Happy exploring! 🧪*
```

---
