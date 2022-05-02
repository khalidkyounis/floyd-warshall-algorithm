""" Recursive version of Floyd-Warshall Algorithm in Python """


def floyd_warshall(dist):
    """ Main function to the shortest path """

    # Get the number of vertices of the input graph
    vertices = len(dist)

    # Define recursive formula for finding
    # the shortest path between two vertices

    def floyd_warshall_rec(i, j, k):

        # Return weight when there are no intermediary vertices
        # This is when k == -1 since index 0 is first vertex
        if k == -1:
            return dist[i][j]

        # If travelling via k is shorter return shorter distance
        else:
            return min(floyd_warshall_rec(i, j, k - 1),
                       floyd_warshall_rec(i, k, k - 1) + floyd_warshall_rec(k,
                                                                            j,
                                                                            k - 1))

    # Find the shortest path and update graph
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                dist[i][j] = floyd_warshall_rec(i, j, k)
            # Return the shortest path graph
    return dist
