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
