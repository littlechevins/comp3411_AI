#!/usr/bin/env python3

# I need to create new array 80x80 that is filled with X's
# instead of adding new parts, we just update and replace :)

# 5 x 5

# +-----+
# |  k  |
# |     |
# |  ^  |
# |     |
# |*****|
# +-----+

# 5 x 5 to the right

# +-----+
# |*    |
# |*    |
# |* ^ k|
# |*    |
# |*    |
# +-----+

import numpy as np

NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3


class Map:

    FOWARD = 'f'
    LEFT = 'l'
    RIGHT = 'r'
    CUT = 'c'
    UNLOCK = 'u'

    NORTH = 0
    EAST  = 1
    SOUTH = 2
    WEST  = 3

    viewWidth = 5
    viewHeight = 5
    charOffset = 2 # character is 2 away from all edges but specifically the left edge

    direction = 0

    last_move = ''

    MAX_SIZE = 80
    UNEXPLORED_BLOCK = '?'

    TREE = 'T'
    DOOR = '-'
    WATER = '~'
    WALL = '*'

    AXE = 'a'
    KEY = 'k'
    STONE = 'o'
    TREASURE = '$'

    hasKey = False
    hasAxe = False
    hasTreasure = False
    numStones = 0

    locX = 0
    locY = 0

    tree_locations = {}
    door_locations = {}
    # water_locations = {}
    axe_locations = {}
    key_locations = {}
    stone_locations = {}
    treasure_locations = {}

    explored_locations = {}



    def map_print(self):
        curr_row = ''
        print("+-----+")
        for row in self.map:
            for col in row:
                curr_row = curr_row + col
            print("|" + curr_row + "|")
            curr_row = ''
        print("+-----+")

    #
    # Removes ^ from the returned view
    #
    @staticmethod
    def removeChararacter(view):

        newArray = np.asarray(view)
        count1 = 0
        count2 = 0
        for row in newArray:
            for ele in row:
                if ele == '^':
                    newArray[count1][count2] = ' '
                    break
                count2 = count2 + 1
            count1 = count1 + 1
            count2 = 0

        return newArray




    #
    # Updates map based on view given, view will overwrite old view in the pos
    #
    def map_update(self, view):

        global locX
        global locY

        rotated_view = view
        if(self.direction == EAST):
            # print("rotating east")
            rotated_view = np.rot90(view, 3)
        elif(self.direction == SOUTH):
            # print("rotating south")
            rotated_view = np.rot90(view, 2)
        elif(self.direction == WEST):
            # print("rotating west")
            rotated_view = np.rot90(view, 1)
        # else:
        #     raise ValueError("Direction not certain/unknown")


        for i in range(0, 5):
          for j in range(0, 5):
            viewBlock = rotated_view[i][j];

            if (i == 2 and j == 2):
                if(self.direction == self.NORTH):
                    viewBlock = '^'
                elif(self.direction == self.EAST):
                    viewBlock = '>'
                elif(self.direction == self.SOUTH):
                    viewBlock = 'v'
                elif(self.direction == self.WEST):
                    viewBlock = '<'


            myX = self.locX + (j - self.charOffset);
            myY = self.locY+ (self.charOffset - i);

            findBlock = (myX, myY)
            self.map[findBlock] = viewBlock
            # if current block is obstacle or tool, we add its location
            self.add_special_object(viewBlock, findBlock)

    #
    # if current block is obstacle or tool, we add its location
    #
    def add_special_object(self, viewBlock, findBlock):

        # print("SPECIAL:" + viewBlock + ".")
        if(viewBlock == self.TREE):
            self.tree_locations[findBlock] = viewBlock
        elif(viewBlock == self.DOOR):
            self.door_locations[findBlock] = viewBlock
        elif(viewBlock == self.AXE):
            self.axe_locations[findBlock] = viewBlock
        elif(viewBlock == self.KEY):
            self.key_locations[findBlock] = viewBlock
        elif(viewBlock == self.STONE):
            self.stone_locations[findBlock] = viewBlock
        elif(viewBlock == self.TREASURE):
            self.treasure_locations[findBlock] = viewBlock

    # NOT SAFE OPERATION, do not delete block that doesnt exist
    # NOT USED
    def remove_special_object(self, viewBlock, findBlock):
        if(viewBlock == self.TREE):
            del self.tree_locations[findBlock]
        elif(viewBlock == self.DOOR):
            del self.door_locations[findBlock]
        elif(viewBlock == self.AXE):
            del self.axe_locations[findBlock]
        elif(viewBlock == self.KEY):
            del self.key_locations[findBlock]
        elif(viewBlock == self.STONE):
            del self.stone_locations[findBlock]
        elif(viewBlock == self.TREASURE):
            del self.treasure_locations[findBlock]

    # dont use yet
    def object_exists(self, dataType, location):
        for x in self.dataType:
            if(x == location):
                return 1
        return 0

    #
    # Updates the character position and type depending on the given action
    #
    def mov_update(self, action):

        self.last_move = action

        if(action == self.FOWARD):

            if(self.collission_detect() == 0):
                if(self.direction == NORTH):
                    self.locY = self.locY + 1
                    self.explored_locations[(self.locX, self.locY)] = self.map[(self.locX, self.locY)]
                elif(self.direction == EAST):
                    self.locX = self.locX + 1
                    self.explored_locations[(self.locX, self.locY)] = self.map[(self.locX, self.locY)]
                elif(self.direction == SOUTH):
                    self.locY = self.locY - 1
                    self.explored_locations[(self.locX, self.locY)] = self.map[(self.locX, self.locY)]
                elif(self.direction == WEST):
                    self.locX = self.locX - 1
                    self.explored_locations[(self.locX, self.locY)] = self.map[(self.locX, self.locY)]
                else:
                    raise ValueError("Direction not certain/unknown")


        elif(action == self.LEFT):

            self.rotateDirection(self.LEFT)
        elif(action == self.RIGHT):

            self.rotateDirection(self.RIGHT)


    #
    # returns tuple of (object, coord) of the object in front
    #
    def get_object_front(self):
        if(self.direction == NORTH):
            blockAheadX = self.locX
            blockAheadY = self.locY + 1
        elif(self.direction == EAST):
            blockAheadX = self.locX + 1
            blockAheadY = self.locY
        elif(self.direction == SOUTH):
            blockAheadX = self.locX
            blockAheadY = self.locY - 1
        elif(self.direction == WEST):
            blockAheadX = self.locX - 1
            blockAheadY = self.locY
        else:
            raise ValueError("Direction not certain/unknown")

        return (self.map[(blockAheadX, blockAheadY)], (blockAheadX, blockAheadY))

    #
    # Rotate direction of the view given the direction of our character
    # since our direction is a number we just just mod it to change left n right
    def rotateDirection(self, dir):
        if(dir == self.LEFT):
            self.direction = (self.direction - 1) % 4
        if(dir == self.RIGHT):
            self.direction = (self.direction + 1) % 4

    # same as above but with num of rotations
    def rotateDirectionNum(self, dir, num):
        count = 0
        for count in range(0, num):
            if(dir == self.LEFT):
                self.direction = (self.direction - 1) % 4
            if(dir == self.RIGHT):
                self.direction = (self.direction + 1) % 4

    #
    # Detects if the block in front is an obstacle or not
    #
    def collission_detect(self):
        blockAheadX = self.locX
        blockAheadY = self.locY

        if(self.direction == NORTH):
            blockAheadX = self.locX
            blockAheadY = self.locY + 1
        elif(self.direction == EAST):
            blockAheadX = self.locX + 1
            blockAheadY = self.locY
        elif(self.direction == SOUTH):
            blockAheadX = self.locX
            blockAheadY = self.locY - 1
        elif(self.direction == WEST):
            blockAheadX = self.locX - 1
            blockAheadY = self.locY
        else:
            raise ValueError("Direction not certain/unknown")

        findBlock = (blockAheadX, blockAheadY)
        blockAhead = self.map[findBlock]
        # print("Block in front is:" + blockAhead + ".")

        if(blockAhead == self.WALL):
            # print("Wall detected")
            return 1
        elif(blockAhead == self.TREE):
            # print("Tree detected")
            return 1
        elif(blockAhead == self.DOOR):
            # print("Door detected")
            return 1

        return 0


    #
    # Prints 12x12 size of map
    #
    def print_map(self):

        print_size = 12

        line = ""
        print("*" * (print_size+1) * 2)
        for y in range(print_size, -print_size, -1):
            for x in range(-print_size, print_size):
                line = line + self.map[(x,y)]
            print('|' + line + '|')
            line = ""
        print("*" * (print_size+1) * 2)



    #
    # Checks if a coordinate is a neighbour to current position
    #
    def is_neighbour(self, coord):
        if(locX + 1 == coord[0]):
            return True
        elif(locX - 1 == coord[0]):
            return True
        elif(locY + 1 == coord[1]):
            return True
        elif(locY - 1 == coord[1]):
            return True
        else:
            return False

    #
    # Takes in a coordinate and depending on character direction and pos, will return a movement based on where the coordinate specifies
    #
    def coord2Action(self, coord):

        action = []

        # neighbour to right
        if(self.locX + 1 == coord[0]):
            if(self.direction == NORTH):
                # turn right, forward
                action.append('r')
                action.append('f')
            elif(self.direction == EAST):
                # forward
                action.append('f')
            elif(self.direction == SOUTH):
                # turn left, forward
                action.append('l')
                action.append('f')
            elif(self.direction == WEST):
                # turn left twice, forward
                action.append('l')
                action.append('l')
                action.append('f')
        elif(self.locX - 1 == coord[0]):
            if(self.direction == NORTH):
                # turn left, forward
                action.append('l')
                action.append('f')
            elif(self.direction == EAST):
                # turn left twice, forward
                action.append('l')
                action.append('l')
                action.append('f')
            elif(self.direction == SOUTH):
                # turn right, forward
                action.append('r')
                action.append('f')
            elif(self.direction == WEST):
                # forward
                action.append('f')
        elif(self.locY + 1 == coord[1]):
            if(self.direction == NORTH):
                # forward
                action.append('f')
            elif(self.direction == EAST):
                # turn left , forward
                action.append('l')
                action.append('f')
            elif(self.direction == SOUTH):
                # turn left twice, forward
                action.append('l')
                action.append('l')
                action.append('f')
            elif(self.direction == WEST):
                # turn right, forward
                action.append('r')
                action.append('f')
        elif(self.locY - 1 == coord[1]):
            if(self.direction == NORTH):
                # turn left twice, forward
                action.append('l')
                action.append('l')
                action.append('f')
            elif(self.direction == EAST):
                # turn right, forward
                action.append('r')
                action.append('f')
            elif(self.direction == SOUTH):
                # forward
                action.append('f')
            elif(self.direction == WEST):
                # turn left, forward
                action.append('l')
                action.append('f')
        elif(self.locY == 0 and self.locX == 0):
                # print("first loc 0,0")
                action.append('l')
                action.append('f')
                # print(action)
        else:
            return []
        return action


    #
    # Getters and Setters
    #

    def get_key_locations(self):
        return self.key_locations

    def get_tree_locations(self):
        return self.tree_locations

    def get_door_locations(self):
        return self.door_locations

    def get_axe_locations(self):
        return self.axe_locations

    def get_stone_locations(self):
        return self.stone_locations

    def get_treasure_locations(self):
        return self.treasure_locations

    def get_has_key(self):
        return self.hasKey

    def get_has_axe(self):
        return self.hasAxe

    def set_has_key(self, set):
        self.hasKey = set

    def set_has_axe(self, set):
        self.hasAxe = set

    def get_tile(self, x, y):
        return self.map[(x,y)]

    def get_has_treasure(self):
        return self.hasTreasure

    def set_has_treasure(self, set):
        self.hasTreasure = set

    def get_self_coord(self):
        return (self.locX, self.locY)

    def get_num_stones(self):
        return self.numStones

    def get_explored_locations(self):
        return self.explored_locations

    def get_neighbours(self):
        block = [self.locX, self.locY]
        neighbours = []

        # for i in range(0, 3):
        neighbours.append((block[0]+1, block[1]))
        neighbours.append((block[0]-1, block[1]))
        neighbours.append((block[0], block[1]+1))
        neighbours.append((block[0], block[1]-1))
        return neighbours

    def get_neighboursGiven(self, block):
        neighbours = []

        # for i in range(0, 3):
        neighbours.append((block[0]+1, block[1]))
        neighbours.append((block[0]-1, block[1]))
        neighbours.append((block[0], block[1]+1))
        neighbours.append((block[0], block[1]-1))
        return neighbours


    #
    # Tests if the block in front is passable or not
    # Not used
    def legal_move(self, tileInFront):
        if(tileInFront == self.WALL):
            return False
        elif(tileInFront == self.KEY):
            if(hasKey):
                return True
            else:
                return False
        elif(tileInFront == self.AXE and hasAxe):
            if(hasAxe):
                return True
            else:
                return False
        else:
            return True


    #
    # Tests if tile is passable depending on tools held
    #
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




    def __init__(self):

        self.map = {}
        for x in range(-self.MAX_SIZE, self.MAX_SIZE):
          for y in range(-self.MAX_SIZE, self.MAX_SIZE):
            self.map[(x,y)] = self.UNEXPLORED_BLOCK

        direction = NORTH


# TESTS BELOW. IGNORE

def main():



    init = np.array([[' ', ' ', 'k', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '^', ' ', ' '], [' ', ' ', ' ', ' ', ' '], ['*', '*', '*', '*', '*']])
    map = Map()

    # we remove the character that displays player location
    # map.map_init(map.removeChararacter(init))


    currDir = 0
    currView = np.array([[' ', ' ', ' ', ' ', ' '], [' ', ' ', 'k', ' ', ' '], [' ', ' ', '^', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])

    downView = np.array([[' ', ' ', 'k', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '^', ' ', ' '], ['*', '*', '*', '*', '*'], [' ', ' ', ' ', ' ', ' ']])

    leftView = np.array([[' ', ' ', ' ', ' ', ' '], [' ', 'k', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])

    emptyView = np.array([[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])


    upsideDownPlusOne = np.array([['*', '*', '*', '*', '*'], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '^', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', 'k', ' ', ' ']])


    # map.rotateView(currView)
    # print(leftView.shape)
    # print(pos[0])

    # map.map_print()

    # map.map_update(currView, currDir, pos)
    # map.map_print()
    #
    # map.map_update(downView, 3, pos)
    # map.map_print()
    #
    # map.map_update(leftView, 1, pos)
    # map.map_print()

    # print("new patch")
    # map.checkPatch(upsideDownPlusOne, currDir, pos)
    # map.map_print()

    map.map_update(currView)
    map.print_map()
    # locY = locY + 1
    # map.map_update(downView)
    # map.print_map()
    map.mov_update(0)
    map.map_update(emptyView)
    map.print_map()

    # print("testing direction")
    # print(map.direction)
    # map.rotateDirection(map.LEFT)
    # print(map.direction)
    # map.rotateDirection(map.LEFT)
    # print(map.direction)
    # map.rotateDirection(map.LEFT)
    # print(map.direction)
    # map.rotateDirection(map.LEFT)
    # print(map.direction)


if __name__ == "__main__":
    main()
    #     # map_array = np.array(ndmin = 2)
    #     # map_array = np.array([['?','?','?','?'], ['?','?','?','?'], ['?','?','?','?']])
    #     # # print map_array
    #     # print(map_array.shape)
    #     # print(map_array)
    #
    #     # still 2d array but we just add new rows as a new array
    #     map = np.empty((0,5), int)
    #
    #     # |  k  |
    #     # |     |
    #     # |  ^  |
    #     # |     |
    #     # |*****|
    #     init = np.array([[' ', ' ', 'k', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '^', ' ', ' '], [' ', ' ', ' ', ' ', ' '], ['*', '*', '*', '*', '*']])
    #     # init = [['0', '0', '0', '0'], ['1', '1', '1', '1'], ['2', '2', '2', '2'], ['3', '3', '3', '3']]
    #
    #     # map_print(init)
    #     map_init(map, init)


# map = np.empty((0,5), int)
# init = np.array([[' ', ' ', 'k', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '^', ' ', ' '], [' ', ' ', ' ', ' ', ' '], ['*', '*', '*', '*', '*']])
# myMap = Map(map, init)
# myMap.map_init(map, init)
