from math import inf, sqrt
from heapq import heappop, heappush


def find_path(src_pt, dst_pt, mesh):
    """
    Function should return two values
        path: a list of points like [(x1,y1), (x2,y2)]
        visited_nodes: a list of boxes explored by the algorithm identified by
        their bounds (x1,y1, x2,y2) - this is the same as mesh format
    In p3_interactive.py it will be called like this
        path, visited_nodes = p3_pathfinder.find_path(src_pt, dst_pt, mesh)
    """

    # path = []
    # visited = []

    search_algorithm = dijkstras(src_pt, dst_pt, mesh, navigation_edges)
    path, visited = search_algorithm
    return path, visited
    pass

# Most likely currently not working because it still needs modification


def dijkstras(src_pt, dst_pt, mesh, adj):

    """

    Args:
        src_pt: Starting point
        dst_pt: Destination point
        mesh: Mesh bitmap
        adj: Navigation_edges passed in as an argument

    Returns: The shortest path from src_pt to dst_pt using
    Dijkstra's shortest path algorithm.

    """

    # precise x,y position within box that path will traverse
    detail_points = {}

    # finds the boxes in which the points reside
    src_box = find_box(src_pt, mesh)
    dst_box = find_box(dst_pt, mesh)

    # Initial distance for starting position
    dist = {src_box: 0}
    prev = {src_box: None}

    path = []
    visited = []
    queue = []

    queue = [(0, src_box)]

    while queue:
        # Continue with next min unvisited node
        curr_distance, curr_node = heappop(queue)
        print("curr_node: " +  str(curr_node))

        # Early termination check: if the dst_pt is found, return the path
        if curr_node == dst_box:
            node = dst_box
            path = []
            while node is not None:
                path.append(node)
                node = prev[node]
            return path[::-1], visited
        for adjacent_node, edge_cost in adj(mesh, curr_node):
            new_distance = curr_distance + edge_cost
            if adjacent_node not in dist or new_distance < dist[adjacent_node]:
                dist[adjacent_node] = new_distance
                prev[adjacent_node] = curr_node
                heappush(queue, (new_distance, adjacent_node))
    # Failed to find a path
    print("Failed to find a path from", src_pt, "to", dst_pt)
    return None
    pass


def navigation_edges(mesh, box):
    """ Provides a list of adjacent cells and their respective costs from the given box.

    Args:
        mesh: A loaded mesh, containing walls, spaces, and waypoints.
        box: A target location.

    Returns:
        A list of tuples containing an adjacent box's coordinates and the cost of the edge joining it and the
        originating box.

        E.g. from (0,0):
            [((0,1), 1),
             ((1,0), 1),
             ((1,1), 1.4142135623730951),
             ... ]
    """

    result = []
    for b in mesh['adj'][box]:
        a = 1/(box[1] - box[0] * box[3] - box[2])
        result.append((b, a))
    return result

    pass


def in_box(point, box):
    """
    Args:
        point: A point on the mesh
        box: A box in the mesh

    Returns: A true or false of whether the point is in a box

    Checks to see whether a point is within a box

    """

    # x and y coordinates
    x = point[0]
    y = point[1]

    # x1 and y1 coordinates of box
    b_x1 = box[0]
    b_y1 = box[2]

    # x2 and y2 coordinates of box
    b_x2 = box[1]
    b_y2 = box[3]

    # Checking to see if point is within box
    if b_x1 <= x <= b_x2:
        if b_y1 <= y <= b_y2:
            return True
        else:
            return False
    pass


def find_box(point, mesh):
    """
    Args:
        point: A point on the mesh
        mesh: The mesh bitmap

    Returns: The box in which the point lies.

    Iterates through the boxes in the mesh to see in which box it lies.

    """

    boxes = mesh['boxes']

    for box in boxes:
        if in_box(point, box):
            return box
    return None


def euclidian_dist(b1, b2):
    dx = b1[0] - b2[0]
    dy = b1[1] - b2[2]

    prod = sqrt(dx*dx + dy*dy)
    return prod
    pass


def aStar():

    pass