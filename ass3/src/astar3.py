#!/usr/bin/env python3

class Astar:

    # https://rosettacode.org/wiki/A*_search_algorithm#Python

    def search(self, start, end, hasKey, hasAxe):
        G = {}
        F = {}

        #Initialize starting values
        G[start] = 0
        F[start] = self.heuristic(start, end)

        closedVertices = set()
        openVertices = set([start])
        cameFrom = {}

        while len(openVertices) > 0:
    		#Get the vertex in the open list with the lowest F score
            current = None
            currentFscore = None
            for pos in openVertices:
                if current is None or F[pos] < currentFscore:
                    currentFscore = F[pos]
                    current = pos

    		#Check if we have reached the goal
            if current == end:
    			#Retrace our route backward
                path = [current]
                while current in cameFrom:
                    current = cameFrom[current]
                    path.append(current)
                path.reverse()
                return path, F[end] #Done!

    		#Mark the current vertex as closed
            openVertices.remove(current)
            closedVertices.add(current)

    		#Update scores for vertices near the current position
            for neighbour in self.map.get_neighboursGiven(current):
                if neighbour in closedVertices:
                    continue #We have already processed this node exhaustively

                print("testing passable:" + str(map.get_tile(neighbour)))
                if (not self.map.isTilePassable(neighbour, hasKey, hasAxe, 0)):
                    print("not passable")
                  continue

                candidateG = G[current] + 1 # graph.move_cost(current, neighbour)

                if neighbour not in openVertices:
                    openVertices.add(neighbour) #Discovered a new vertex
                elif candidateG >= G[neighbour]:
                    continue #This G score is worse than previously found

    			#Adopt this G score
                cameFrom[neighbour] = current
                G[neighbour] = candidateG
                H = self.heuristic(neighbour, end)
                F[neighbour] = G[neighbour] + H

        raise RuntimeError("A* failed to find a solution")

        # closedSet = set()
        #
        # # openSet = queue.PriorityQueue()
        # openSet = set([start])
        #
        # cameFrom = {}
        # self.gScore[start] = 0
        # self.fScore[start] = self.heuristic_cost_estimate(start, goal)
        # print("fscore start")
        # print(self.fScore[start])
        #
        # while len(openSet) > 0:
        #
        #     current = None
        #     currentFScore = None
        #     for pos in openSet:
        #         print("pos")
        #         print(pos)
        #         if current is None or self.fScore[pos] < currentFScore:
        #             print(self.fScore)
        #             currentFScore = self.fScore[pos]
        #             current = pos
        #         print("current fscore" + str(currentFScore))
        #         print("current" + str(current))
        #         print("fscorepos" + str(self.fScore[pos]))
        #
        #
        #     if current == goal:
        #         #Retrace our route backward
        #         path = [current]
        #         while current in cameFrom:
        #             current = cameFrom[current]
        #             path.append(current)
        #         path.reverse()
        #         return path, self.fScore[end] #Done!
        #
        #
        #     openSet.remove(current)
        #     closedSet.add(current)
        #
        #
        #     for neighbour in self.get_neighbours(current):
        #
        #         if neighbour in closedSet:
        #             continue
        #
        #         candidateG = self.gScore[current] + 1
        #
        #         if neighbour not in openSet:
        #             openSet.add(neighbour)
        #         elif candidateG >= self.gScore[neighbour]:
        #             continue #This G score is worse than previously found
        #
    	# 		#Adopt this G score
        #         cameFrom[neighbour] = current
        #         self.gScore[neighbour] = candidateG
        #         heuristicFound = self.heuristic_cost_estimate(neighbour, goal)
        #         self.gScore[neighbour] = self.gScore[neighbour] + heuristicFound
        #
        # raise RuntimeError("A* failed to find a solution")


    def heuristic(self, start, goal):
        # we use manhattan distance since it is admissible due to not horizontal movement
        # print("heuristic is:" + str(abs(start[0] - goal[0]) + abs(start[1] - goal[1])))
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    # def get_neighbours(self, block):
    #     neighbours = []
    #     # for i in range(0, 3):
    #     neighbours.append((block[0]+1, block[1]))
    #     neighbours.append((block[0]-1, block[1]))
    #     neighbours.append((block[0], block[1]+1))
    #     neighbours.append((block[0], block[1]-1))
    #     return neighbours

    # def reconstruct_path(cameFrom, current)
    #     total_path := {current}
    #     while current in cameFrom.Keys:
    #         current := cameFrom[current]
    #         total_path.append(current)
    #     return total_path


    def __init__(self, map): # , start, goal
        print("init astar3")
        self.map = map
        # self.gScore = {}
        # self.fScore = {}
        # self.start = start
        # self.goal = goal

def main():
    ast = Astar()
