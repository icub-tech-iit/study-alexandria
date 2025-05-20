from setuptools import setup, find_packages

setup(
    name="sysmlv2parser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime",
        "antlr4-tools"
    ],
    description="A parser for SysML v2 models",
    author="Martina Gloria",
    author_email="martina.gloria@iit.it",
    python_requires=">=3.6",
)