from setuptools import setup

setup(
    name="elemdex",
    version="0.1.0",
    author="cvetyshayasiren",
    description="CLI tool for exploring chemical elements",
    py_modules=["elemdex", "find", "utils"],
    package_data={
        "": ["data.json"],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "elemdex=elemdex:main",
        ],
    },
    python_requires=">=3.6",
)
