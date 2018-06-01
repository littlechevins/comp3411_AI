#!/usr/bin/env python3

import queue
import random
import map2
import astar
# maps = map2.Map()
pendingMoves = queue.Queue()
actionsSoFar = []


class Move:


    # coordMoves = moves.spiral((5,5), (0,0))


    def moveChar(self):

        print(self.maps.get_explored_locations())
        # print("next unexploreed move:" + str(makeMoveUnexplored()))
        # return makeMoveRandom()
        # return makeMoveSpiral()

        print("Object in front:" + self.maps.get_object_front()[0] + ".")
        print("key hashmap:" + str(self.maps.get_key_locations()))
        print("tree hashmap:" + str(self.maps.get_tree_locations()))
        print("door hashmap:" + str(self.maps.get_door_locations()))
        print("axe hashmap:" + str(self.maps.get_axe_locations()))
        print("stone hashmap:" + str(self.maps.get_stone_locations()))
        print("treasure hashmap:" + str(self.maps.get_treasure_locations()))

        # final_string = self.makeMoveUnexplored()
        final_string = self.makeMoveRandom()
        print("running atar")
        self.ast.search((0,0), (1,1))
        print("stopping astar")

        # if(final_string == 'f'):
        #     if(maps.get_object_front()[0] == 'k'):
        #         maps.remove_special_object('k', maps.get_object_front()[1])
        #     elif(maps.get_object_front()[0] == 'o'):
        #         maps.remove_special_object('o', maps.get_object_front()[1])
        #     elif(maps.get_object_front()[0] == 'a'):
        #         maps.remove_special_object('a', maps.get_object_front()[1])
        #     elif(maps.get_object_front()[0] == '$'):
        #         maps.remove_special_object('$', maps.get_object_front()[1])
        # elif(final_string == 'c'):
        #     if(maps.get_object_front()[0] == 'T'):
        #         maps.remove_special_object('T', maps.get_object_front()[1])
        # elif(final_string == 'u'):
        #     if(maps.get_object_front()[0] == '-'):
        #         maps.remove_special_object('-', maps.get_object_front()[1])
        # return final_string[0]

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
                        elif(final_string == 'u'):
                            if(self.maps.get_object_front()[0] == '-'):
                                self.maps.remove_special_object('-', self.maps.get_object_front()[1])
                        return final_string[0]

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

    def __init__(self, globalMap):
        print("Move init")
        self.maps = globalMap
        self.ast = astar.Astar(self.maps)


# def main():
#     m = Move()
#     myList = m.spiral((5,5), (0,0))
#     print(myList)
#
# if __name__ == "__main__":
#     main()
