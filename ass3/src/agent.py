#!/usr/bin/python3
# ^^ note the python directive on the first line
# COMP 9414 agent initiation file
# requires the host is running before the agent
# designed for python 3.6
# typical initiation would be (file in working directory, port = 31415)
#        python3 agent.py -p 31415
# created by Leo Hoare
# with slight modifications by Alan Blair

# Modified by Kevin Luo

##MAKEFILE##
# I wasn't able to create a makefile for an agent executable unless I hardcoded a port in.
# You can run my agent using: 'python3 agent.py -p *PORT*'

# PROGRAM DESCRIPTION

# Our program first creates an instance of map and updates its current view and location depending on its last move. On initiation, these do nothing. We then create an instance of our move class and call a function to move our character. In our move function, we randomly step around 1000 times to explore the map. We avoid water during this step. With our surroundings explored, we use astar to nagivate to a door/tree if we have the correct tools. We then perform our action on the object and continue on. Our astar algorithm has a special case where if the object is not passable, we go to the next avaliable neighbour.
#
# Our data structure for the global map is a hashmap containing coordinates and the object at its location: eg {(x,y), 'k'}. We also store hashmaps of notable objects, ie, keys, doors, stones, etc
#
# My move class has a pendingMoves queue which we add or delete from so that new instances of possible moves do not affect the queued up moves.
#
# We implemented a floodfill algorithm for better nagivation but this was not used due to lack of avaliable time.
#
# Overall my program does not yet successfully nagivate water at a passable rate. This was due to time constraints




import sys
import socket

import map
import move


# declaring visible grid to agent
view = [['' for _ in range(5)] for _ in range(5)]
maps = map.Map()
moves = move.Move(maps)


# Returns a action for the agent to perform
def get_action(view, lastAction):


    maps.mov_update(lastAction)

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
