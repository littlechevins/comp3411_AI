def movetodoor(Map,DoorLocation):  #call

    current = (Map.locX, Map.locY)

    movelist = a_star_search(current,DoorLocation)

    #append turn to door + U(unlock) to movelist

    return(coord2Action(movelist))

def movetotree(Map,TreeLocation):

    current = (Map.locX, Map.locY)

    movelist = a_star_search(current,TreeLocation)

    #append turn to tree + C(chop) to movelist

    return(coord2Action(movelist))
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


    def IsReachable(self,Map,start,goal,hasKey,hasAxe):
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
