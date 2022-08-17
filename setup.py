#!/usr/bin/python3

import os
import setuptools
import setuptools.command.install

f = open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"),
    encoding="ascii",
)
readme = f.read()
f.close()

setuptools.setup(
    name="freewvs",
    version="0.1.3",
    description="A free web vulnerability scanner",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://freewvs.schokokeks.org/",
    packages=[],
    scripts=["freewvs", "update-freewvsdb"],
    python_requires=">=3",
    license="0BSD",
    keywords=["security", "vulnerability", "web"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: 0BSD",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
