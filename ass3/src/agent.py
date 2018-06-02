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
import move


# declaring visible grid to agent
view = [['' for _ in range(5)] for _ in range(5)]
maps = map2.Map()
moves = move.Move(maps)
# pos = [0,0]


# function to take get action from AI or user
def get_action(view, lastAction):

    ## REPLACE THIS WITH AI CODE TO CHOOSE ACTION ##
    # print("before loc:" + str(maps.get_self_coord()))
    # print("updating move:" + str(lastAction))
    maps.mov_update(lastAction)
    # print("current loc:" + str(maps.get_self_coord()))

    maps.map_update(view)

    maps.print_map()

    return moves.moveChar()



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
