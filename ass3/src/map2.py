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

    # global MAX_SIZE
    # global UNEXPLORED_BLOCK
    # global direction
    # global NORTH
    # global EAST
    # global SOUTH
    # global WEST

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

    hasKey = True
    hasAxe = False
    numStones = 0

    locX = 0
    locY = 0

    tree_locations = {}
    # tree_locations2 = []
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



    # |CXXXCXXXXXXXXXXXXX
    # |  k  |
    # |     |
    # |  ^  |
    # |     |
    # |*****|
    # +-----+
    # checks all the chars in the area marked between c's
    def isExplored(self, pos, square):

        # currLocLeft = self.map[pos[0] + 2][pos[1] - 2]
        # currLocRight = self.map[pos[0] + 2][pos[1] + 2]

        # currLocLeft = (pos[1] - 2)
        # currLocRight = (pos[1] + 2)

        # check = 0
        # for check < 5:
        #     if(self.map[pos[0] + 2][pos[1] - 2 + check] == 'X')
        # print("checking if explored:" + self.map[pos[0] - 2][pos[1] - 2 + square] + ".")
        if(self.map[pos[0] - 2][pos[1] - 2 + square] == 'X'):
            return 0
        return 1



    # # pass in the action and the returned view of the 5x5
    # we move the agent pointer to the given position from the centre

    # since we only every look forward, we only need view[0]
    # we add 'X' buffer to map when we update array since we must maintain the shape of np array.

    # use pos, then go to the coord and count +2 in what ever direction and check if that row of 5 contains any x, if it does its unexplored, if it doesnt then dont worry

    # @staticmethod
    def map_update(self, view):

        global locX
        global locY
        # if(direction == NORTH):
        # if its north then we do nothing

        # i forgot to set rotate_view = bla
        # i was just assigning np to nothing so it was broken before :(
        rotated_view = view
        if(self.direction == EAST):
            print("rotating east")
            rotated_view = np.rot90(view, 3)
        elif(self.direction == SOUTH):
            print("rotating south")
            rotated_view = np.rot90(view, 2)
        elif(self.direction == WEST):
            print("rotating west")
            rotated_view = np.rot90(view, 1)
        # else:
        #     raise ValueError("Direction not certain/unknown")

        # update the map a block at a time

        print(self.locX)
        print(self.locY)

        for i in range(0, 5):
          for j in range(0, 5):
            viewBlock = rotated_view[i][j];

            # player tile
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


    # if current block is obstacle or tool, we add its location
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

    # dont use until i figure out how to pass by reference in python
    def object_exists(self, dataType, location):
        for x in self.dataType:
            if(x == location):
                return 1
        return 0

    def mov_update(self, action):

        self.last_move = action

        if(action == self.FOWARD):
            # what is current direction
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
            print("left action")
            self.rotateDirection(self.LEFT)
        elif(action == self.RIGHT):
            print("right action")
            self.rotateDirection(self.RIGHT)
        # elif(action == CHOP):
        #
        # else(action == UNLOCK):

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

    # since our direction is a number we just just mod it to change left n right
    def rotateDirection(self, dir):
        if(dir == self.LEFT):
            self.direction = (self.direction - 1) % 4
        if(dir == self.RIGHT):
            self.direction = (self.direction + 1) % 4

    def rotateDirectionNum(self, dir, num):
        count = 0
        for count in range(0, num):
            if(dir == self.LEFT):
                self.direction = (self.direction - 1) % 4
            if(dir == self.RIGHT):
                self.direction = (self.direction + 1) % 4

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
            print("Wall detected")
            return 1
        elif(blockAhead == self.TREE):
            print("Tree detected")
            return 1
        elif(blockAhead == self.DOOR):
            print("Door detected")
            return 1

        return 0


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



    # def rotateView(self, view):
    #
    #     print(view)
    #
    #     # newArray = np.empty((0,5), int)
    #     #
    #     # for i in range(0,view.shape[0]):
    #     #     for j in range(view.shape[1]-1, 0):
    #     #         newArray[i][j] = view[j][i];
    #     print(np.rot90(view))
    #     # print(view)



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

    # code is long af and messy af but cbf to make pretty
    def coord2Action(self, coord):
        # if is_neighbour(coord):
        # Testing if neighbour then changing direction on case by case
        action = []
        # print("my coord: " + str(self.locX) + ", " + str(self.locY))
        # print("given coord: " + str(coord[0]) + ", " + str(coord[1]))

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
                print("first loc 0,0")
                action.append('l')
                action.append('f')
                # print(action)
        else:
            print("FOUND NONE???")
            return []
        return action



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

    def get_tile(self, x, y):
        return self.map[(x,y)]

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

    # randomly explore
    # if found key then astar to door
    # if found axe then astar to tree
    #


    def __init__(self):

        print("Generating map")
        # self.map = np.full((MAX_SIZE * 2, MAX_SIZE * 2), UNEXPLORED_BLOCK)

        self.map = {}
        for x in range(-self.MAX_SIZE, self.MAX_SIZE):
          for y in range(-self.MAX_SIZE, self.MAX_SIZE):
            # this.map.put(new Point2D.Double(x, y), OBSTACLE_UNKNOWN);
            self.map[(x,y)] = self.UNEXPLORED_BLOCK

        # print(self.map)
        print("Printing map")
        self.print_map()

        direction = NORTH

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


##################################Shiwei added here#####################################



def main():

    # global locX
    # global locY

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
