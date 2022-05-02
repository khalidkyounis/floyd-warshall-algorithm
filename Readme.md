<img src="https://www.liverpool.ac.uk/logo-size-test/full-colour.svg" alt="mypy logo" width="300px"/>

# Recursive version of Floyd-Warshall Algorithm in Python

## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Unit Test](#unittest)
- [cProfile (Pefromance Test)](#cprofile)
- [Contributing](#contributing)
- [License](#license)

<a name="background"/>

## Background

This application is to find the shortest distances between vertices. The function is written in recursive method as part of solving Mid-Module Assignment of the Software Development in Practice module at the University of Liverpool.

<a name="install"/>

## Install

To clone the project, using following link of porject directory to the IDE:

   [ https://github.com/khalidkyounis/floyd-warshall-algorithm.git]( https://github.com/khalidkyounis/floyd-warshall-algorithm.git " https://github.com/khalidkyounis/floyd-warshall-algorithm.git")


To install the required packages to run the application, write below command in the terminal:

    pip install -r requirements.txt

<a name="usage"/>

## Usage

Type the below command to execute the program:

    python test_recursive.py

<a name="unittest"/>

## Unit Test

To perform Unit Test for the data samples in test_samples.py file, type the following command in the IDE terminal or Run the code directly:

    python -m unittest tests/unit_test_recursive.py

<a name="cprofile"/>

## cProfile (Pefromance Test)

To test the performance of recursive and imperative version of Floyd-Warshall functions, type the following command in the IDE terminal or Run the code directly:

    python -m cProfile tests/performance_test_recursive.py

<a name="contributing"/>

## Contributing

Any contribution to improve the application is possible.

<a name="license"/>

## License

[MIT](LICENSE) © Khalid Younis
