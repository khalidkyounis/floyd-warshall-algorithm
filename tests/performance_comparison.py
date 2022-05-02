"""Compare the performance of recursive versus imperative using
Brute Force methodology """

# Import built-in packages
import sys
import time

# This is used because the function file is not in the path where recursive
# and imperative functions are so when searching from tests folder it looks
# only for files in same directory as it
sys.path.append('.')

# Import functions from functions folder
import functions.floyd_warshall_imperative
import functions.floyd_warshall_recursive


def performance_comparison():
    """Define function to calculate the execution time of recursive and
    imperative functions """

    inf = 99999
    graph = [[0, 5, inf, 10],
             [inf, 0, 3, inf],
             [inf, inf, 0, 1],
             [inf, inf, inf, 0]
             ]

    started_at = time.time()
    for _ in range(2 ** 12):
        functions.floyd_warshall_recursive.floyd_warshall(graph)
    elapsed_recursive_time = time.time() - started_at

    started_at = time.time()
    for _ in range(2 ** 12):
        functions.floyd_warshall_imperative.floyd_warshall(graph)
    elapsed_imperative_time = time.time() - started_at

    return elapsed_recursive_time, elapsed_imperative_time


if __name__ == '__main__':
    elapsed_recursive, elapsed_imperative = performance_comparison()

    # Print the comparison between both versions in seconds
    print('Recursive: ', round(elapsed_recursive, 2), 'seconds')
    print('Imperative: ', round(elapsed_imperative, 2), 'seconds')
