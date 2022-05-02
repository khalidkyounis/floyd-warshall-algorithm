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

This repository is to implement the Floyd-Warshall algorithm in Python to find the shortest distances between vertices. The function is written in the recursive method as part of solving the Mid-Module Assignment of the Software Development in Practice module at the University of Liverpool. There are also performance test codes that are performed on pre-defined data sets using Python built-in packages Unit Test and cProfile. The application was developed using PyCharm Community Edition IDE.

<a name="install"/>

## Install

To clone the project, use the following link for the project directory to the IDE:

   [ https://github.com/khalidkyounis/floyd-warshall-algorithm.git]( https://github.com/khalidkyounis/floyd-warshall-algorithm.git " https://github.com/khalidkyounis/floyd-warshall-algorithm.git")


To install the required packages to run the application, write below command in the terminal:

    pip install -r requirements.txt

<a name="usage"/>

## Usage

Type the below command to execute the program:

    python test_recursive.py

<a name="unittest"/>

## Unit Test

To perform Unit Test for the data samples in test_samples.py file, type the following command in the IDE terminal or run the code directly:

    python -m unittest tests/unit_test_recursive.py

<a name="cprofile"/>

## cProfile (Pefromance Test)

To test the performance of recursive and imperative version of Floyd-Warshall functions, type the following command in the IDE terminal or run the code directly:

    python -m cProfile tests/performance_test_recursive.py

<a name="contributing"/>

## Contributing

Any contribution to improve the application is possible.

<a name="license"/>

## License

[MIT](LICENSE) © Khalid Younis
