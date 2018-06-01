#!/usr/bin/env python3

import map2
import queue
# map = map2.Map()

class Astar:

    # f(n) = g(n) + h(n)

    gScore = {}
    fScore = {}
    INFINITY = 9999999
    MAX_SIZE = 80

    searchExhausted = False

    # def heuristic(a, b):
    # (x1, y1) = a
    # (x2, y2) = b
    # return abs(x1 - x2) + abs(y1 - y2)

    # def a_star_search(graph, start, goal):


    # *******************
    # start = (x,y)
    # goal  = (x,y)
    def search(self, start, goal):


        # The set of nodes already evaluated
        closedSet = {}

        # The set of currently discovered nodes that are not evaluated yet.
        # Initially, only the start node is known.
        openSet = queue.PriorityQueue()
        # openSet.put(start, 0)

        # For each node, which node it can most efficiently be reached from.
        # If a node can be reached from many nodes, cameFrom will eventually contain the
        # most efficient previous step.
        cameFrom = {}

        # For each node, the cost of getting from the start node to that node.
        # For each node, the total cost of getting from the start node to the goal
        # by passing by that node. That value is partly known, partly heuristic.

        for y in range(self.MAX_SIZE, -self.MAX_SIZE, -1):
          for x in range(-self.MAX_SIZE, self.MAX_SIZE):
            self.gScore[(x,y)] = self.INFINITY
            self.fScore[(x,y)] = self.INFINITY

        # print("set g and f scores to infinite")

        # The cost of going from start to start is zero.
        self.gScore[start] = 0;

        # print("establishing gscore start")

        # For the first node, that value is completely heuristic.
        self.fScore[start] = self.heuristic_cost_estimate(start, goal)
        openSet.put(start)

        # print("fscore at start is heuristic to goal")

        while not openSet.empty():

            # print("contents of openset")
            # print(openSet)
            # the node in openSet having the lowest fScore[] value
            current = openSet.get()
            # print("current:" + str(current))
            # print("goal:" + str(goal))
            if current == goal:
                print("current is goal!!!!!!!!!!!!!")
                searchExhausted = True
                return
                # return reconstruct_path(cameFrom, current)


            closedSet[current] = self.map.get_tile(current[0], current[1])

            # for each neighbor of current
            print("current:" + str(current))
            print("neighbours:" + str(self.get_neighbours(current)))
            for neighbour in self.get_neighbours(current):
                # print("current is:" + str(current))
                # print("neighbour is:" + str(neighbour))
                if neighbour in closedSet:
                # Ignore the neighbor which is already evaluated.
                    continue

                if neighbour in openSet.queue:	# Discover a new node
                    continue
                    # openSet.put(neighbour)

                # // The distance from start to a neighbor
                # //the "dist_between" function may vary as per the solution requirements.
                tentative_gScore = self.gScore[current] + 1
                if tentative_gScore >= self.gScore[neighbour]:
                    continue # This is not a better path.
                print("tentative score:" + str(tentative_gScore))

                # // This path is the best until now. Record it!
                cameFrom[neighbour] = current
                self.gScore[neighbour] = tentative_gScore
                self.fScore[neighbour] = tentative_gScore + self.heuristic_cost_estimate(neighbour, goal)

            if (neighbour not in openSet.queue):
                openSet.put(neighbour)

        # return failure
        searchExhausted = True

    def heuristic_cost_estimate(self, start, goal):
        # we use manhattan distance since it is admissible due to not horizontal movement
        print("heuristic is:" + str(abs(start[0] - goal[0]) + abs(start[1] - goal[1])))
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def get_neighbours(self, block):
        neighbours = []
        # for i in range(0, 3):
        neighbours.append((block[0]+1, block[1]))
        neighbours.append((block[0]-1, block[1]))
        neighbours.append((block[0], block[1]+1))
        neighbours.append((block[0], block[1]-1))
        return neighbours

    # def reconstruct_path(cameFrom, current)
    #     total_path := {current}
    #     while current in cameFrom.Keys:
    #         current := cameFrom[current]
    #         total_path.append(current)
    #     return total_path


    def __init__(self, map): # , start, goal

        self.map = map
        # self.start = start
        # self.goal = goal

def main():
    ast = Astar()
