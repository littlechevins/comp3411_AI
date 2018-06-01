
 def isTilePassable(tile,hasKey,hasAxe):
     return (  (tile == State.OBSTACLE_SPACE) or/   # all these state.XXXX is to be replaced by map setting
               (tile == State.OBSTACLE_STEPPING_STONE_PLACED) or/
               (tile == State.OBSTACLE_TEMPORARY_WATER) or/
               (tile == State.TOOL_AXE) or/
               (tile == State.TOOL_KEY) or/
               (tile == State.TOOL_GOLD) or/
               (tile == State.TOOL_STEPPING_STONE) or/
               ((tile == State.OBSTACLE_DOOR) and hasKey) or/
               ((tile == State.OBSTACLE_TREE) and hasAxe) or/
               (tile == State.DIRECTION_UP) or/
               (tile == State.DIRECTION_DOWN) or/
               (tile == State.DIRECTION_LEFT) or/
               (tile == State.DIRECTION_RIGHT)
             )


def IsReachable(map,start,goal,hasKey,hasAxe):
     q = queue.Queue()
     isConnected=set()

     q.add(start)

     while(not q.empty()):
         first = q.get()

         tile = getchar(map,first);
         if(first not in isConnected):
             if(not isTilePassable(tile,hasKey,hasAxe))
                 continue

             isConnected.add(first)

             for i in range(4):
                 neighbourX = first.getX();  #key of first is X,Y coordinate
                 neighbourY = first.getY();

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
             neighbout = (str(neighbourX)+str(neighbourY))
             if (neighbour not in isConnected):
                 q.add(neighbour)


     return(goal in isConnected)
########################################################################################
