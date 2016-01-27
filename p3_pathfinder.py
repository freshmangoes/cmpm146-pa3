from math import inf, sqrt
from heapq import heappop, heappush


def find_path(src_pt, dst_pt, mesh):
    """

    Args:
        src_pt: Starting point of search
        dst_pt: Destination point of search
        mesh: Mesh object taken from .gif file

    Returns: Path - the path from src_pt to dst_pt and visited - a list of visited boxes

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

    # finds the boxes in which the points reside
    src_box = find_box(src_pt, mesh)
    dst_box = find_box(dst_pt, mesh)

    dist = {src_box: 0}
    prev_box = {src_box: None}
    queue = [(0, src_box)]

    visited = []
    prev_box[src_box] = None
    detail_pt = {src_box: src_pt}

    dist[src_pt] = 0

    while queue:
        curr_distance, curr_node = heappop(queue)

        curr_x1 = curr_node[0]
        curr_x2 = curr_node[1]

        print("curr_node: " + str(curr_node))
        curr_distance = dist[curr_node]
        visited.append(curr_node)

        if curr_node == dst_box:
            node = dst_box
            path = [node]
            # path, node = [(detail_pt[node, dst_pt])], node
            print("node: " + str(node))

            while node is not None and prev_box[node] is not None:
                # if node is not None:
                print("prev_box[node]: " + str(prev_box[node]))
                path.append(((node[0], node[2]), (node[1], node[3])))
                # path.append((prev_box[curr_x2], curr_x2))
                node = prev_box[node]
                visited.append(node)
            print("path: " + str(path))
            return path[-2::-1], visited
        for adjacent_node in mesh['adj'][curr_node]:
        # for adjacent_node, edge_cost in adj(mesh, curr_node):
            # new_distance = curr_distance + edge_cost
            new_distance = curr_distance + dist[curr_node]
            if adjacent_node not in dist or new_distance < dist[adjacent_node]:
                dist[adjacent_node] = new_distance
                prev_box[adjacent_node] = curr_node
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
        a = 1/((b[1] - b[0]) * (b[3] - b[2]))
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

    # x = point[1]
    # y = point[0]
    #
    # b_x1 = box[2]
    # b_y1 = box[0]
    #
    # b_x2 = box[3]
    # b_y2 = box[1]


    # Checking to see if point is within box

    # if b_x1 <= x and x >= b_x2:
    #     if b_y1 <= y and y>= b_y2:
    #         return True
    # else:
    #     return False

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


def a_star(src_pt, dst_pt, mesh):
    pass
