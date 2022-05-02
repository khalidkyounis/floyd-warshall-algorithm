""" Imperative version of Floyd-Warshall Algorithm in Python """


def floyd_warshall(graph):
    """Solves all pair the shortest path via Floyd Warshall Algorithm"""
    vertices = len(graph)
    assert all(len(row) == vertices for row in graph)

    # distance[][] will be the output matrix that will finally
    # have the shortest distances between every pair of vertices
    # initializing the solution matrix same as input graph matrix
    # OR we can say that the initial values of the shortest distances
    # are based on shortest paths considering no intermediate vertices

    distance = [row[:] for row in graph]

    for k in range(vertices):
        # pick all vertices as source one by one
        for i in range(vertices):
            # Pick all vertices as destination for the
            # above picked source
            for j in range(vertices):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                distance[i][j] = min(distance[i][j],
                                     distance[i][k] + distance[k][j])

                # Return the shortest path graph

    return distance
