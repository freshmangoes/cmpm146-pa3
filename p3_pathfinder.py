from math import inf, sqrt
from heapq import heappop, heappush


def find_path(src_pt, dst_pt, mesh):
    # src_pt is an (x,y) pair
    # dst_pt is an (x,y) pair
    # mesh is a mesh data structure

    """
    Function should return two values
        path: a list of points like [(x1,y1), (x2,y2)]
        visited_nodes: a list of boxes explored by the algorithm identified by
        their bounds (x1,y1, x2,y2) - this is the same as mesh format
    In p3_interactive.py it will be called like this
        path, visited_nodes = p3_pathfinder.find_path(src_pt, dst_pt, mesh)
    """
    path = []
    visited = []

    boxes = mesh['boxes']
    adj = mesh['adj']

    print(adj(1))

    # path, visited = dijkstras(src_pt, dst_pt, boxes, adj)
    return path, visited
    pass

# Most likely currently not working because it still needs modification


def dijkstras(src_pt, dst_pt, mesh, adj):
    # precise x,y position within box that path will traverse
    # detail_points = { }

    # finds the boxes in which the points reside
    src_box = find_box(src_pt, mesh)
    dst_box = find_box(dst_pt, mesh)

    if (src_box is None) or (dst_box is None):
        print("No path possible")
        return [],[]

    distances = {src_box: 0}           # Table of distances to cells
    previous_cell = {src_box: None}    # Back links from cells to predecessors
    box_coord = {src_box: src_pt}
    queue = [src_box]   # initialize queue as the start box

    # Initial distance for starting position
    distances[src_box] = 0

    while queue:
        # Continue with next min unvisited node
        current_distance, current_node = heappop(queue)

        # Early termination check: if the dst_pt is found, return the path
        if current_node == dst_pt:
            node = dst_pt
            path = [node]
            while node is not None:
                path.append(previous_cell[node])
                node = previous_cell[node]
            return path[::-1]

        # Calculate tentative distances to adjacent cells
        for adjacent_node, edge_cost in adj(mesh, current_node):
            new_distance = current_distance + edge_cost

            if adjacent_node not in distances or new_distance < distances[adjacent_node]:
                # Assign new distance and update link to previous cell
                distances[adjacent_node] = new_distance
                previous_cell[adjacent_node] = current_node
                heappush(queue, (new_distance, adjacent_node))

    # Failed to find a path
    print("Failed to find a path from", src_pt, "to", dst_pt)
    return None
    pass


# Modify adjacency function to take in boxes
def navigation_edges(level, cell):
    """ Provides a list of adjacent cells and their respective costs from the given cell.

    Args:
        level: A loaded level, containing walls, spaces, and waypoints.
        cell: A target location.

    Returns:
        A list of tuples containing an adjacent cell's coordinates and the cost of the edge joining it and the
        originating cell.

        E.g. from (0,0):
            [((0,1), 1),
             ((1,0), 1),
             ((1,1), 1.4142135623730951),
             ... ]
    """
    x, y = cell
    spaces = level['boxes']
    adjacent_nodes = {}

    for delta_x in [-1, 0, 1]:
        for delta_y in [-1, 0, 1]:
            next_cell = (x + delta_x, y + delta_y)
            if next_cell != cell and next_cell in spaces:
                distance = sqrt(delta_x ** 2 + delta_y ** 2)
                adjacent_nodes[next_cell] = distance * (spaces[cell] + spaces[next_cell])/2

    return adjacent_nodes.items()


def in_box(point, box):
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
    # Find the box the point is in
    # iterate through boxes in mesh
    for box in mesh['boxes']:
        if in_box(point, box):
            return box
    return None



def aStar():

    pass