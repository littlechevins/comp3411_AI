
  
def isTilePassable(tile,hasKey,hasAxe,stone):  ###stone is the number of stone agent has
    if (tile == '~' && stone>0):
        return 'stone'
    else:
        return (  (tile == ' ') ||/
                  (tile == 'O') ||/
                  (tile == 'a') ||/
                  (tile == 'k') ||/
                  (tile == '$') ||/
                  (tile == 'o') ||/
                  ((tile == '-') && hasKey) ||/
                  ((tile == 'T') && hasAxe) ||
                )


def IsReachable(Map,start,goal,hasKey,hasAxe,stone):
    
    q = queue.Queue()
    isConnected=set()
        
    q.add(start)
        
    while(!q.empty()):
        first = q.get()
            
        tile = Map.map[first]
        if(first not in isConnected):
            checkstone = isTilePassable(tile,hasKey,hasAxe,stone)
            if(!checkstone):
                continue
            elif (checkstone == 'stone'):
                stone = stone - 1
                
            isConnected.add(first)
                
            for i in range(4):
                neighbourX = first[0];  #key of first is X,Y coordinate
                neighbourY = first[1];
                
                if i == 0:
                    neighbourX += 1
                    break
                elif i == 1:
                    neighbourX -= 1
                    break
                elif i == 2:
                    neighbourY += 1
                    break
                elif i == 3:
                    neighbourY -= 1
                    break
            neighbour = (str(neighbourX)+str(neighbourY))
            if (neighbour not in isConnected):
                q.add(neighbour)
                
        
    return(goal in isConnected)


     return(goal in isConnected)
########################################################################################
