"""Test Samples for testing Floyd-Warshall"""

# This file contains three different test samples of the Floyd-Warshall
# algorithm with the expected outputs to be used by performance test
# techniques.


# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other
INF = 99999

# Test 1: Small data set
sample_1 = [[0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]]

result_1 = [[0, 5, 8, 9],
            [INF, 0, 3, 4],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]]

# Test 2: Negative Edges Graph
sample_2 = [[0, INF, 2, INF],
            [4, 0, 3, INF],
            [INF, INF, 0, 2],
            [INF, -2, INF, 0]]

result_2 = [[0, 2, 2, 4],
            [4, 0, 3, 5],
            [4, 0, 0, 2],
            [2, -2, 1, 0]]

# Test 3: Large data set
sample_3 = [[0, 3, 8, INF, -4],
            [INF, 0, INF, 1, 7],
            [INF, 4, 0, INF, INF],
            [2, INF, -5, 0, INF],
            [INF, INF, INF, 6, 0]]

result_3 = [[0, 1, -3, 2, -4],
            [3, 0, -4, 1, -1],
            [7, 4, 0, 5, 3],
            [2, -1, -5, 0, -2],
            [8, 5, 1, 6, 0]]
