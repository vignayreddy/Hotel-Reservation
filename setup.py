from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-HOTEL-RESERVATION",
    version="0.1",
    author="VignayReddy",
    packages = find_packages(),
    install_requires= requirements,
)