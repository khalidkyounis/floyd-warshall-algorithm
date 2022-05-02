# Test Samples for testing Floyd-Warshall

""" This file contains four different test cases for the Floyd Warshall
algorithm function.   The function works for all types of graphs
including ones with negative edges, except if the graph contains a
negative cycle.  Below is the expected inputs and outputs for each
different scenario.
"""

""" This file include """
# Use value for infinity to denote edges that do not exist
INF = 99999

# Test A: Control Graph
""" Title: Floyd Warshall Algorithm | DP-16
Author: GeeksforGeeks
Date: 24th Nov. 2021
Code version: unknown
Availability: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
"""

# Test 1: Negative Edges Graph (No Negative Cycles)
sample_1 = [[0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]]

result_1 = [[0, 5, 8, 9],
            [INF, 0, 3, 4],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]]

# Test 2: Negative Edges Graph (No Negative Cycles)
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
