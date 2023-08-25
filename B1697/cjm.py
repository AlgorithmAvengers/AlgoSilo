import sys
from collections import deque

SB, kid = map(int, sys.stdin.readline().strip().split())

if SB == kid:
    print(0)
    exit(0)

bfs = deque()
bfs.append((SB, 0))
wayDict = {}
while bfs.__len__() > 0:
    # print("들어와따!")
    temp = bfs.popleft()
    # print(temp)
    for i in [-1, 1, temp[0]]:
        nextSB = temp[0] + i
        if nextSB == kid:
            print(temp[1] + 1)
            bfs = deque()
            break
        else:
            if nextSB >= 0 and nextSB not in wayDict:
                bfs.append((temp[0]+i, temp[1]+1))
                wayDict[nextSB] = True
            
