from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A simple, lightweight hangman game made in python!'

# Setting up
setup(
    name="hangman",
    version=VERSION,
    author="Jack Grant",
    author_email="<classifiedcontentonyt@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'game', 'terminal', 'simple', 'hangman', 'lightweight'],
    classifiers=[
        "Development Status :: Released",
        "Intended Audience :: Average Coder",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
