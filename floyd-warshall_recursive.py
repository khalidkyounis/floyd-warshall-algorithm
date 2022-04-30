# Recursive Version of Floyd Warshall Algorithm

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other

INF = 99999

"""This function is a print function to display the solution 
on the screen using a nested loop"""

"""The outer loop has been coded using python's built in 
function range(). It iterates over the number of vertices 
that will be passed to the parameter V. In this case 
the number will be 4 since there are 4 vertices"""

"""The inner loop will execute each vertices in the outer loop 
4 times, and if there is no path between the beginning vertices 
and the destination vertices, it will print INF. If there is, it 
will print the distance between each pair of vertices """


def printSolution(V, dist):
    print("Following matrix shows the shortest distances"
          "between every pair of vertices\n")
    for i in range(V):

        # It takes all vertices from the graph's columns (labeled as j)
        for j in range(V):

            # If there is no direct path between two vertices it prints INF
            if dist[i][j] == INF:
                print("INF", end=" ")

            # If there is a path between two vertices,
            # it will print the distance
            else:
                print(dist[i][j], end="  ")
        print(" ")


"""This is the main recursive function. The function in this case will 
not only take the number of vertices (4) and the graph, but will also 
include a parameter (counter) to keep track of how many times is the function 
calling itself. When it reaches the beginning it will stop, if not, it will 
keep on calling itself"""


def floydWarshallRec(V, graph, count):
    dist = graph

    # if count===V is the base case for the recursion.
    # If the counter reaches the number of vertices, the function will stop
    if count == V:
        printSolution(V, dist)

        """for the else statement, the triple loop on the original iterative 
        function has been maintained, where the distances between i and j 
        will be rewritten. """

        """The outer loop has been coded using python's built-in function 
        range(). The function range() iterates over the number of vertices 
        that will be passed to the parameter numOfvertices. In this case the 
        number will be 4 since there are 4 vertices """
    else:

        # it takes all vertices one by one and
        # sets them as intermediate vertices
        for k in range(V):

            # It takes al vertices from the graph's rows (labeled as i)
            for i in range(V):

                # It takes al vertices from the graph's columns (labeled as j)
                for j in range(V):
                    """if the distance between any two vertices using an 
                    intermediate vertex is lesser that the direct distance 
                    between two vertices without an intermediate vertex. The 
                    min() built in function returns the distance with the 
                    lowest value """
                    dist[i][j] = min(dist[i][j],
                                     dist[i][k] + dist[k][j])

            """The last line on the function is where the recursion 
            is executed. Now that the distances have been rewritten 
            with the lowest distance value, the function calls itself 
            again. It maintains the same number of vertices but with 
            the changed distance parameters. The counter parameter keeps 
            track of how many times the function has been called. Every 
            time the function calls itself again, it will have done it once 
            more, hence it becomes we add +1 to the counter parameter"""

        floydWarshallRec(V, dist, count + 1)


"""The floydWarshallRec function takes three parameters, so another 
function without the counter parameter needs to be created 
in order to get the output for the graph. floydWarshall calls 
FloydWarshallRec with the counter set to value 0"""


def floydWarshall(V, graph):
    floydWarshallRec(V, graph, 0)


graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]

# Print the solution
floydWarshall(4, graph)

# We use timeit module to measure the execution time
# to test the performance of the recursive code
if __name__ == "__main__":
    import timeit

    print("_____________\n")
    print("Testing recursive performance using timeit:")
    print(timeit.timeit())
