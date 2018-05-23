#!/usr/bin/env python3

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

# @staticmethod
def array2np(array):
    # arr = np.empty((0,5), int)
    # for ele in array:
    #     arr = np.append(arr, ele)

    # arr = arr.reshape(0,5)
    # arr = np.array([array[0], array[1], array[2], array[3], array[4]])
    arr = np.asarray(array)
    return arr

def array2npBuffer(array, size):
    print("input size: " + str(size))
    buffer = 0
    arr = np.empty((0,size), int)
    for ele in array:
        arr = np.append(arr, ele)
        buffer = buffer + 1

    while buffer < size:
        arr = np.append(arr, 'X')
        buffer = buffer + 1

    print(arr)
    print(arr.shape)

    return arr

class Map:

    viewWidth = 5
    viewHeight = 5
    charOffset = 2 # character is 2 away from all edges but specifically the left edge



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

    # map is global map that we create
    # view is local map of what we get from console
    def map_init(self, view):

        # print(view.shape)
        # print(self.map.shape)


        for row in view:
            self.map = np.vstack((self.map,row))

        self.map_print()


    # # pass in the action and the returned view of the 5x5
    # we move the agent pointer to the given position from the centre

    # since we only every look forward, we only need view[0]
    # we add 'X' buffer to map when we update array since we must maintain the shape of np array.

    # use pos, then go to the coord and count +2 in what ever direction and check if that row of 5 contains any x, if it does its unexplored, if it doesnt then dont worry

    # @staticmethod
    def map_update(self, view, direction, pos):
        cx = pos[0]
        cy = pos[1]
        # print(pos[0])

        if(direction == NORTH):
            print("NORTH")
            # add to top of map,  horizontal
            # for now assume unexplored

            myarray = array2np(view[0])
            # add to front of array
            self.map = np.vstack((myarray, self.map))
            # self.map_print(self.map)
        elif(direction == EAST):
            print("")
            # add to right of map, vertical

            # we need to pad our array since we must have matching shapes
            if(self.map.shape > view.shape):
                myarray = array2npBuffer(view[0], self.map.shape[0])
                print("Shape not suitable")
                print(self.map.shape[0])
            else:
                myarray = array2np(view[0])
            # add to front of array

            print("map shape: " + str(self.map.shape))
            print("east array shape: " + str(myarray.shape))
            self.map = np.hstack((myarray, self.map))
        elif(direction == SOUTH):
            print("")
            # add to bottom of map,  horizontal
        elif(direction == WEST):
            print("WEST")
            # add to left of map, vertical
            myarray = array2np(view[4])
            # add to back of array
            self.map = np.vstack((self.map, myarray))
        else:
            raise ValueError("Direction not certain/unknown")



    #     for row in view:
    #         for col in row:
    #             map[row_map][col_map] = col
    #             col_map = col_map + 1
    #         row_map = row_map + 1
    #
    #     map_print(map)

    def __init__(self):
        print("Generating map")
        self.map = np.empty((0,5), int)

def main():

    init = np.array([[' ', ' ', 'k', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '^', ' ', ' '], [' ', ' ', ' ', ' ', ' '], ['*', '*', '*', '*', '*']])
    map = Map()

    # we remove the character that displays player location
    map.map_init(map.removeChararacter(init))


    pos = [0,1]

    currDir = 0
    currView = np.array([[' ', ' ', ' ', ' ', ' '], [' ', ' ', 'k', ' ', ' '], [' ', ' ', '^', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])

    downView = np.array([[' ', ' ', 'k', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '^', ' ', ' '], ['*', '*', '*', '*', '*'], [' ', ' ', ' ', ' ', ' ']])

    leftView = np.array([[' ', ' ', ' ', ' ', ' '], [' ', 'k', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])
    # print(leftView.shape)
    # print(pos[0])

    map.map_update(currView, currDir, pos)
    map.map_print()

    map.map_update(downView, 3, pos)
    map.map_print()

    map.map_update(leftView, 1, pos)
    map.map_print()

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
