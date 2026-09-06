from setuptools import setup

setup(
    name="elemdex",
    version="0.1.0",
    author="cvetyshayasiren",
    description="CLI tool for exploring chemical elements",
    py_modules=["elemdex"],
    entry_points={
        "console_scripts": [
            "elemdex=elemdex:main",
        ],
    },
    python_requires=">=3.6",
)