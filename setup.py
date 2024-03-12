"""Python setup.py for net_worth_tracker package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("net_worth_tracker", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="net_worth_tracker",
    version=read("net_worth_tracker", "VERSION"),
    description="Awesome net_worth_tracker created by bkm82",
    url="https://github.com/bkm82/net-worth-tracker/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="bkm82",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["net_worth_tracker = net_worth_tracker.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
