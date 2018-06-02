#!/usr/bin/env python3

import queue
import random
import map2
import astar3
# maps = map2.Map()
pendingMoves = queue.Queue()
actionsSoFar = []


class Move:


    # coordMoves = moves.spiral((5,5), (0,0))


    def moveChar(self):

        # print(self.maps.get_explored_locations())
        # print("next unexploreed move:" + str(makeMoveUnexplored()))
        # return makeMoveRandom()
        # return makeMoveSpiral()

        # print("Object in front:" + self.maps.get_object_front()[0] + ".")
        # print("key hashmap:" + str(self.maps.get_key_locations()))
        # print("tree hashmap:" + str(self.maps.get_tree_locations()))
        # print("door hashmap:" + str(self.maps.get_door_locations()))
        # print("axe hashmap:" + str(self.maps.get_axe_locations()))
        # print("stone hashmap:" + str(self.maps.get_stone_locations()))
        # print("treasure hashmap:" + str(self.maps.get_treasure_locations()))
        # print("has key:" + str(self.maps.get_has_key()))
        # print("has axe:" + str(self.maps.get_has_axe()))


        # final_string = self.makeMoveUnexplored()

        # do random moves for 30 turns
        # if found key and astar can find a path then take it and open
        # if found axe and astar can find path then take it
            # if we have also found tree then astar to tree and cut


        # print("running atar")
        # start = (0,0)
        # goal = (7,7)
        # cameFrom, costSoFar = self.ast.search(start, goal)
        # print(cameFrom)
        # print("stopping astar")

        # print("testing is passable")
        # tile = '*'
        # test = self.maps.isTilePassable(tile,False,False,0)
        # print(test)
        # print("fin test passable")


        # full explore map without doing anything undoable
        if(self.numMoves < 1000):
            print("random move:" + str(self.numMoves))
            final_string = self.makeMoveRandom()
        else:
            final_string = self.makeMoveSeekNGo()

        # print("final string is:" + str(final_string))



        if(final_string == 'f'):
            if(self.maps.get_object_front()[0] == 'k'):
                self.maps.remove_special_object('k', self.maps.get_object_front()[1])
                self.maps.set_has_key(True)
            elif(self.maps.get_object_front()[0] == 'o'):
                self.maps.remove_special_object('o', self.maps.get_object_front()[1])
            elif(self.maps.get_object_front()[0] == 'a'):
                self.maps.remove_special_object('a', self.maps.get_object_front()[1])
                self.maps.set_has_axe(True)
            elif(self.maps.get_object_front()[0] == '$'):
                self.maps.remove_special_object('$', self.maps.get_object_front()[1])
        elif(final_string == 'c'):
            if(self.maps.get_object_front()[0] == 'T'):
                self.maps.remove_special_object('T', self.maps.get_object_front()[1])
                self.maps.set_has_axe(False)
                # force it go to into the recently opened path
                pendingMoves.queue.clear()
                pendingMoves.put('f')
        elif(final_string == 'u'):
            if(self.maps.get_object_front()[0] == '-'):
                self.maps.remove_special_object('-', self.maps.get_object_front()[1])
                self.maps.set_has_key(False)
                pendingMoves.queue.clear()
                pendingMoves.put('f')
        self.numMoves = self.numMoves + 1
        return final_string[0]

        # not used vvv
        # input loop to take input from user (only returns if this is valid)
        while 1:
            inp = input("Enter Action(s): ")
            inp.strip()
            final_string = ''
            for char in inp:
                if char in ['f','l','r','c','u','b','F','L','R','C','U','B']:
                    final_string += char
                    if final_string:
                            # important!!
                            # if next action is f and we have key/stone/axe in front of us, we must remove from list
                        if(final_string == 'f'):
                            if(self.maps.get_object_front()[0] == 'k'):
                                self.maps.remove_special_object('k', self.maps.get_object_front()[1])
                            elif(self.maps.get_object_front()[0] == 'o'):
                                self.maps.remove_special_object('o', self.maps.get_object_front()[1])
                            elif(self.maps.get_object_front()[0] == 'a'):
                                self.maps.remove_special_object('a', self.maps.get_object_front()[1])
                            elif(self.maps.get_object_front()[0] == '$'):
                                self.maps.remove_special_object('$', self.maps.get_object_front()[1])
                        elif(final_string == 'c'):
                            if(self.maps.get_object_front()[0] == 'T'):
                                self.maps.remove_special_object('T', self.maps.get_object_front()[1])
                                pendingMoves.put('f')
                        elif(final_string == 'u'):
                            if(self.maps.get_object_front()[0] == '-'):
                                self.maps.remove_special_object('-', self.maps.get_object_front()[1])
                                pendingMoves.put('f')
                        return final_string[0]

    def makeMoveSeekNGo(self):

        cutTrigger = False
        unlockTrigger = False
        # coordMoves = []

        if(self.maps.get_has_key()):
            if self.maps.get_door_locations():
                # print(self.maps.get_door_locations())
                door_loc = next(iter(self.maps.get_door_locations()))
                # print("astar to door")
                # print("current:" + str(self.maps.get_self_coord()))
                # print("doorloc:" + str(door_loc))
                coordMoves, costSoFar = self.ast.search(self.maps.get_self_coord(), door_loc, self.maps.get_has_key(), self.maps.get_has_axe())
                # coordMoves.append('u')
                unlockTrigger = True
                # print("astar to door:" + str(coordMoves))
            else:
                # print("empty key")
                # print("KEY RANDOM CHOICE")
                neighbours = self.maps.get_neighbours()
                coordMoves = random.sample(neighbours, 2)

        elif(self.maps.get_has_axe()):

            if self.maps.get_tree_locations():
                # print("astar to tree")
                # print("current:" + str(self.maps.get_self_coord()))
                tree_loc = next(iter(self.maps.get_tree_locations()))
                # print("treeloc:" + str(tree_loc))
                coordMoves, costSoFar = self.ast.search(self.maps.get_self_coord(), tree_loc, self.maps.get_has_key(), self.maps.get_has_axe())
                # coordMoves.append('c')
                cutTrigger = True
                # print("astar to tree:" + str(coordMoves))
            else:
                # print("empty axe")
                # print("AXE RANDOM CHOICE")
                neighbours = self.maps.get_neighbours()
                coordMoves = random.sample(neighbours, 2)
        else:
            # just set coordmoves to random until we find a key
            # print("ELSE RANDOM CHOICE")
            neighbours = self.maps.get_neighbours()
            coordMoves = random.sample(neighbours, 2)


        while(self.maps.get_self_coord() == coordMoves[0]):
            coordMoves.pop(0)
        else:
            # print("print coordmoves")
            # print(coordMoves)
            action = coordMoves.pop(0)
            # print("action")
            # print(action)
            sequence = self.maps.coord2Action(action)
            if(cutTrigger):
                sequence.append('c')
            if(unlockTrigger):
                sequence.append('u')
        # print("sequence")
        # print(sequence)
        # print("end seq")
        if(pendingMoves.empty()):
            for seq in sequence:
                pendingMoves.put(seq)
            # print("coord pending")
            # print(pendingMoves)
            # print("end pendingMoves")
            tmp = pendingMoves.get()
            actionsSoFar.append(tmp)
            # print("returning seq:" + str(tmp))
            # print("pending moves after:" + str(pendingMoves))
            return tmp
        else:
            # print("pendingMoves moves")
            # print(pendingMoves)
            # print("end pendingMoves")
            tmp = pendingMoves.get()
            actionsSoFar.append(tmp)
            return tmp

    # def test():
    #     print("test")
    def makeMoveSpiral(self):

        coordMoves = spiral((5,5), (0,0))

        print(actionsSoFar)
        # print(coordMoves.pop(0))
        while(self.maps.get_self_coord() == coordMoves[0]):
            coordMoves.pop(0)
        else:
            sequence = self.maps.coord2Action(coordMoves.pop(0))
        print("sequence")
        print(sequence)
        print("end seq")
        if(pendingMoves.empty()):
            for seq in sequence:
                pendingMoves.put(seq)
            print("coord moves")
            print(coordMoves)
            print("end")
            tmp = pendingMoves.get()
            actionsSoFar.append(tmp)
            return tmp
        else:
            print("coord moves")
            print(coordMoves)
            print("end")
            tmp = pendingMoves.get()
            actionsSoFar.append(tmp)
            return tmp

    def makeMoveRandom(self):
        choices = ['f','l','r']# , 'c', 'u'
        return (random.choice(choices))

    def makeMoveUnexplored(self):
        # print("my pos:" + str(maps.get_self_coord()))
        # print("my nei:" + str(maps.get_neighbours()))
        neighbours = self.maps.get_neighbours()
        goto = []
        for block in neighbours:
            # if(maps.get_explored_locations() == block):
            if(block in self.maps.get_explored_locations()):
                continue
            else:
                goto.append(block)


        print("goto")
        print(goto)
        # return (random.choice(goto))

        sequence = self.maps.coord2Action(random.choice(goto))
        if(pendingMoves.empty()):
            for seq in sequence:
                pendingMoves.put(seq)
            tmp = pendingMoves.get()
            actionsSoFar.append(tmp)
            return tmp
        else:
            tmp = pendingMoves.get()
            actionsSoFar.append(tmp)
            return tmp


    def spiral(self, start, pos):
        # x = y = 0
        X = start[0]
        Y = start[1]
        x = pos[0]
        y = pos[1]
        dx = 0
        dy = -1
        list = []
        for i in range(max(X, Y)**2):
            if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
                # print (x, y)
                list.append((x,y))
                # DO STUFF...
            if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
                dx, dy = -dy, dx
            x, y = x+dx, y+dy
        return list

    ###############
    def isTilePassable(self,tile,hasKey,hasAxe,stone):  ###stone is the number of stone agent has
        if (tile == '~' and stone>0):
            return 'stone'
        else:
            return (  (tile == ' ') or\
                      (tile == 'O') or\
                      (tile == 'a') or\
                      (tile == 'k') or\
                      (tile == '$') or\
                      (tile == 'o') or\
                      ((tile == '-') and hasKey) or\
                      ((tile == 'T') and hasAxe) or\
                      (tile == '^')or\
                      (tile == 'v') or\
                      (tile == '<') or\
                      (tile == '>'))


    def IsReachable(self,Map,start,goal,hasKey,hasAxe):  # work when there is no raft
        stone = Map.numStones
        q = queue.Queue()
        isConnected=set()

        q.put(start)

        while(not q.empty()):
            print([i for i in q.queue])
            print(isConnected)
            first = q.get()

            tile = Map.map[first]

            if(first not in isConnected):
                checkstone = self.isTilePassable(tile,hasKey,hasAxe,stone)
                if(not checkstone):
                    continue
                elif (checkstone == 'stone'):
                    stone = stone - 1

                isConnected.add(first)

                for i in range(4):
                    neighbourX = first[0];  #key of first is X,Y coordinate
                    neighbourY = first[1];

                    if i == 0:
                        neighbourX += 1
                        neighbour = (neighbourX,neighbourY)
                        if (neighbour not in isConnected):
                            q.put(neighbour)
                        continue
                    elif i == 1:
                        neighbourX -= 1
                        neighbour = (neighbourX,neighbourY)
                        if (neighbour not in isConnected):
                            q.put(neighbour)
                        continue
                    elif i == 2:
                        neighbourY += 1
                        neighbour = (neighbourX,neighbourY)
                        if (neighbour not in isConnected):
                            q.put(neighbour)
                        continue
                    elif i == 3:
                        neighbourY -= 1

                        neighbour = (neighbourX,neighbourY)
                        if (neighbour not in isConnected):
                            q.put(neighbour)


        return(goal in isConnected)


    ###############

    def __init__(self, globalMap):
        # print("Move init")
        self.maps = globalMap
        self.ast = astar3.Astar(self.maps)
        self.numMoves = 0


# def main():
#     m = Move()
#     myList = m.spiral((5,5), (0,0))
#     print(myList)
#
# if __name__ == "__main__":
#     main()
