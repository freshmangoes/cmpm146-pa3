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

    # src_pt is an (x,y) pair
    # dst_pt is an (x,y) pair
    # mesh is a mesh data structure

    path = []
    visited = []

    boxes = mesh['boxes']
    adj = mesh['adj']

    # path, visited = dijk(src_pt, dst_pt, mesh, adj)
    path, visited = dijkstras(src_pt, dst_pt, adj)
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

    if (src_box is None) or (dst_box is None):
        print("No path possible")
        return [], []

    dist = {src_box: 0}           # Table of distances to boxes
    prev = {src_box: None}    # Back links from cells to predecessors
    box_coord = {src_box: src_pt}
    queue = [src_box]   # initialize queue as the start box

    # Initial distance for starting position
    dist[src_box] = 0

    path = []
    visited = []

    while queue:
        # Continue with next min unvisited node
        # print(heappop(queue))
        _, curr_box = heappop(queue)

        # Early termination check: if the dst_pt is found, return the path
        if curr_box == dst_pt:
            node = dst_pt
            path = []
            while node is not None:
                path.append(node)
                node = prev[node]
            return path[::-1]

    # Failed to find a path
    print("Failed to find a path from", src_pt, "to", dst_pt)
    return None
    pass

# def navigation_edges(mesh, box):
#     """
#     Args:
#         mesh: The mesh bitmap
#         box: A box
#
#     Returns: A list of adjacent boxes to box
#
#     Finds the neighbors of box and returns them as a list.
#
#     """
#     x1 = box[2]
#     y1 = box[0]
#     x2 = box[3]
#     y2 = box[1]
#
#     adj_boxes = {}
#
#     neighbors = mesh['adj'][box]
#     for n in neighbors:
#         next_box =
#
#     pass

# def navigation_edges(mesh, box):
#
#     x1 = box[2]
#     y1 = box[0]
#     x2 = box[3]
#     y2 = box[1]
#
#     boxes = mesh['boxes']
#     adj_boxes = {}
#     for dx in [-1, 0, 1]:
#         for dy in[ -1, 0, 1]:
#             next_box = (x+dx, y+dy)
#             if next_box != box and next_box in boxes:
#                 dist = sqrt(dx ** 2 + dy ** 2)
#                 adj_boxes[next_box] = dist * (boxes[box] + boxes[next_box])/2
#     return adj_boxes.items()
#
#     pass


def in_box(point, box):
    """
    Args:
        point: A point on the mesh
        box: A box in the mesh

    Returns: A true or false of whether the point is in a box

    Checks to see whether a point is within a box

    """

    # x and y coordinates
    y = point[0]
    x = point[1]

    # x1 and y1 coordinates of box
    b_y1 = box[0]
    b_x1 = box[2]

    # x2 and y2 coordinates of box
    b_y2 = box[1]
    b_x2 = box[3]

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



def aStar():

    pass