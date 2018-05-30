#!/usr/bin/env python3

class Move:

    # def test():
    #     print("test")

    def spiral(self, start, pos):
        # x = y = 0
        X = start[0]
        Y = start[1]
        x = pos[0]
        y = pos[1]
        dx = 0
        dy = -1
        list = []
        for i in range(max(X, Y)**2):
            if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
                # print (x, y)
                list.append((x,y))
                # DO STUFF...
            if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
                dx, dy = -dy, dx
            x, y = x+dx, y+dy
        return list

    def __init__(self):
        print("Move init")

# def main():
#     m = Move()
#     myList = m.spiral((5,5), (0,0))
#     print(myList)
#
# if __name__ == "__main__":
#     main()
