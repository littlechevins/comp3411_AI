#!/usr/bin/env python3

class astar:

    # f(n) = g(n) + h(n)

    gScore = {}
    fScore = {}
    INFINITY = 9999999

    def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(graph, start, goal):



    # *******************
    # start = (x,y)
    # goal  = (x,y)
    def search(start, goal):




    # The set of nodes already evaluated
    closedSet = {}

    # The set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
    openSet = PriorityQueue()
    openSet.put(start, 0)

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    cameFrom = {}

    # For each node, the cost of getting from the start node to that node.
    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.

    for y in range(map.MAX_SIZE, -map.MAX_SIZE, -1):
      for x in range(-map.MAX_SIZE, map.MAX_SIZE):
        gScore[] = self.INFINITY
        fScore[] = self.INFINITY

    # The cost of going from start to start is zero.
    gScore[start] = 0;


    # For the first node, that value is completely heuristic.
    fScore[start] = heuristic_cost_estimate(start, goal)

    while not openSet.empty()
        # the node in openSet having the lowest fScore[] value
        current = openSet.get()
        if current = goal
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        closedSet[current] = None

        # for each neighbor of current
        for neighbour in get_neighbours(current)
            if neighbor in closedSet
            # Ignore the neighbor which is already evaluated.
                continue

            if neighbor not in openSet	// Discover a new node
                openSet.put(neighbor)

            # // The distance from start to a neighbor
            # //the "dist_between" function may vary as per the solution requirements.
            tentative_gScore := gScore[current] + dist_between(current, neighbor)
            if tentative_gScore >= gScore[neighbor]
                continue		// This is not a better path.

            # // This path is the best until now. Record it!
            cameFrom[neighbor] := current
            gScore[neighbor] := tentative_gScore
            fScore[neighbor] := gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)

    return failure

    def heuristic_cost_estimate(start, goal):
        # we use manhattan distance since it is admissible due to not horizontal movement
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def get_neighbours(self, block):
        neighbours = []
        # for i in range(0, 3):
        neighbors.append((block[0]+1, block[1]))
        neighbors.append((block[0]-1, block[1]))
        neighbors.append((block[0], block[1]+1))
        neighbors.append((block[0], block[1]-1))


function reconstruct_path(cameFrom, current)
    total_path := {current}
    while current in cameFrom.Keys:
        current := cameFrom[current]
        total_path.append(current)
    return total_path


    def __init__(self, map, start, goal):

        this.map = map
        this.start = start
        this.goal = goal
