from setuptools import setup, find_packages

setup(
    name="cheatsheets",
    author="Huzaifa Asim",
    maintainer="HunerOn Codes",
    maintainer_email="toyoureply@gmail.com",
    description="Quickly recap syntax of various programming libraries and frameworks with cheat sheets in this Git repository.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/huneron/cheatsheets",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License 2.0",
        "Operating System :: OS Independent :: Windows Recommended",
    ],
    python_requires=">=3.6",
)
