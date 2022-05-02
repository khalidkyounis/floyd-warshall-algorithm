<img src="https://www.liverpool.ac.uk/logo-size-test/full-colour.svg" alt="mypy logo" width="300px"/>

# Recursive version of Floyd-Warshall Algorithm in Python

## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Unit Test](#Unit_Test)
- [cProfile (Pefromance Test)](#cProfile)
- [Contributing](#contributing)
- [License](#license)

## Background

This application is to find the shortest distances between vertices. The function is written in recursive method as part of solving Mid-Module Assignment of the Software Development in Practice module at the University of Liverpool.

## Install

To clone the project, using following link of porject directory to the IDE:

   [ https://github.com/khalidkyounis/floyd-warshall-algorithm.git]( https://github.com/khalidkyounis/floyd-warshall-algorithm.git " https://github.com/khalidkyounis/floyd-warshall-algorithm.git")


To install the required packages to run the application, write below command in the terminal:

    pip install -r requirements.txt

## Usage

Type the below command to execute the program:

    python test_recursive.py

## Unit Test

To perform Unit Test for the data samples in test_samples.py file, type the following command in the IDE terminal or Run the code directly:

    python -m unittest tests/unit_test_recursive.py

## cProfile (Pefromance Test)

To test the performance of recursive and imperative version of Floyd-Warshall functions, type the following command in the IDE terminal or Run the code directly:

    python -m cProfile tests/performance_test_recursive.py

## Contributing

Any contribution to improve the application is possible.

## License

[MIT](LICENSE) © Khalid Younis
