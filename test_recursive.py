"""Test the recursive version of Floyd-Warshall Algorithm"""

# Import the recursive function of Floyd-Warshall

from functions.floyd_warshall_recursive import floyd_warshall

# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other
INF = float('inf')

# Driver program to test the above program
# Let us create the following weighted graph
"""
            10
       (0)------->(3)
        |         /|
      5 |          |
        |          | 1
        |/         |
       (1)------->(2)
            3           """
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]

# Return and print the results
print("Following matrix shows the shortest distances between every pair of "
      "vertices\n")

# Print the result matrix
print(*floyd_warshall(graph), sep="\n")
