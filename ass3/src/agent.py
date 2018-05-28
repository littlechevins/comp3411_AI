#!/usr/bin/python3
# ^^ note the python directive on the first line
# COMP 9414 agent initiation file
# requires the host is running before the agent
# designed for python 3.6
# typical initiation would be (file in working directory, port = 31415)
#        python3 agent.py -p 31415
# created by Leo Hoare
# with slight modifications by Alan Blair

import sys
import socket

import map2

# declaring visible grid to agent
view = [['' for _ in range(5)] for _ in range(5)]
maps = map2.Map()
isInit = 0
# pos = [0,0]

# function to take get action from AI or user
def get_action(view, lastAction):

    ## REPLACE THIS WITH AI CODE TO CHOOSE ACTION ##
    global isInit
    global pos

    print("last action:" + lastAction + ":")



    # # just assume we are always facing north
    # if(lastAction == 'f'):
    #     pos[0] = pos[0] + 1


    # if(isInit == 0):
    #     maps.map_init(maps.removeChararacter(view))
    #     isInit = 1


    # important!!
    # if next action is f and we have key/stone/axe in front of us, we must remove from list

    maps.mov_update(lastAction)
    print("UPDATING MOVE END")

    print("UPDATING VIEW")

    maps.map_update(view)
    print("UPDATING MOVE")


    print("Last action:" + lastAction)

    print("--------------------My Map--------------------")
    maps.print_map()
    print("---------------------END--------------------")

    print("Object in front:" + maps.get_object_front()[0] + ".")
    print("key hashmap:" + str(maps.get_key_locations()))
    print("tree hashmap:" + str(maps.get_tree_locations()))
    print("door hashmap:" + str(maps.get_door_locations()))
    print("axe hashmap:" + str(maps.get_axe_locations()))
    print("stone hashmap:" + str(maps.get_stone_locations()))
    print("treasure hashmap:" + str(maps.get_treasure_locations()))

    # input loop to take input from user (only returns if this is valid)
    while 1:
        inp = input("Enter Action(s): ")
        inp.strip()
        final_string = ''
        for char in inp:
            if char in ['f','l','r','c','u','b','F','L','R','C','U','B']:
                final_string += char
                if final_string:
                    if(final_string == 'f'):
                        if(maps.get_object_front()[0] == 'k'):
                            maps.remove_special_object('k', maps.get_object_front()[1])
                        elif(maps.get_object_front()[0] == 'o'):
                            maps.remove_special_object('o', maps.get_object_front()[1])
                        elif(maps.get_object_front()[0] == 'a'):
                            maps.remove_special_object('a', maps.get_object_front()[1])
                        elif(maps.get_object_front()[0] == '$'):
                            maps.remove_special_object('$', maps.get_object_front()[1])
                    return final_string[0]

# helper function to print the grid
def print_grid(view):
    print('+-----+')
    for ln in view:
        print("|"+str(ln[0])+str(ln[1])+str(ln[2])+str(ln[3])+str(ln[4])+"|")
    print('+-----+')

if __name__ == "__main__":

    # pos[0] = 0
    # pos[1] = 0

    # checks for correct amount of arguments
    if len(sys.argv) != 3:
        print("Usage Python3 "+sys.argv[0]+" -p port \n")
        sys.exit(1)

    port = int(sys.argv[2])

    # checking for valid port number
    if not 1025 <= port <= 65535:
        print('Incorrect port number')
        sys.exit()

    # creates TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
         # tries to connect to host
         # requires host is running before agent
         sock.connect(('localhost',port))
    except (ConnectionRefusedError):
         print('Connection refused, check host is running')
         sys.exit()

    # navigates through grid with input stream of data
    i=0
    j=0
    lastAction = ''
    while 1:
        data=sock.recv(100)
        if not data:
            exit()
        for ch in data:
            if (i==2 and j==2):
                view[i][j] = '^'
                view[i][j+1] = chr(ch)
                j+=1
            else:
                view[i][j] = chr(ch)
            j+=1
            if j>4:
                j=0
                i=(i+1)%5
        if j==0 and i==0:
            print_grid(view) # COMMENT THIS OUT ON SUBMISSION
            lastAction = action = get_action(view, lastAction) # gets new actions
            sock.send(action.encode('utf-8'))

    sock.close()
