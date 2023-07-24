import sys
import collections

N = int(sys.stdin.readline().strip())  # 몇칸인지
pandaLand = []  # 판다랜드
for i in range(N):
    pandaLand.append(list(map(int, sys.stdin.readline().strip().split(" "))))


def check(point):
    currVal = pandaLand[point[0]][point[1]]
    row = point[0]
    col = point[1]
    result = [1, 1, 1, 1]  # 위 아래 왼 오
    if row == 0 or pandaLand[row - 1][col] <= currVal:
        result[0] = 0  # 위는 안돼
    if col == 0 or pandaLand[row][col - 1] <= currVal:
        result[2] = 0  # 왼은 안돼
    if row == N - 1 or pandaLand[row + 1][col] <= currVal:
        result[1] = 0  # 아래는 안돼
    if col == N - 1 or pandaLand[row][col + 1] <= currVal:
        result[3] = 0  # 오른은 안돼
    return result, currVal
    # 그래서 위, 아래, 왼, 오 다 가능하면 [1,1,1,1], 0은 각 위치로는 못 간다는 말.

maxCount = 0
# while len(went) < N**2:
startPoint = set()
wayDict = {}
for row in range(N):
    for col in range(N):
        startPoint.add((row,col))
for point in startPoint:
    if point in wayDict:
        continue
    elif check([point[0], point[1]])[0] == [0,0,0,0]:
        wayDict[point] = 0
        continue
    else:
        pointMax = 0
        stack = collections.deque()  # stack
        stack.appendleft(list(point) + [0, 1])
        stackCount = 1
        while stackCount > 0:
            temp = stack.popleft()
            stackCount -= 1
            currPoint = temp[:2]
            currTuple = tuple(currPoint)
            beforeVal = temp[2]
            beforeCount = temp[3]
            if currTuple in wayDict:
                currCount = wayDict[currTuple] + beforeCount
                if currCount > pointMax:
                    pointMax = currCount
                continue
            else:
                if beforeCount > pointMax:
                    pointMax = beforeCount
            wayTogo, currVal = check(currPoint)
            if wayTogo == [0,0,0,0]:
                wayDict[currTuple] = 0
            for i in range(4):
                if wayTogo[i] == 1:
                    stackCount += 1
                    if i == 0:
                        stack.appendleft([currPoint[0] - 1, currPoint[1], currVal, beforeCount + 1])
                    if i == 1:
                        stack.appendleft([currPoint[0] + 1, currPoint[1],  currVal, beforeCount + 1])
                    if i == 2:
                        stack.appendleft([currPoint[0], currPoint[1] - 1,  currVal, beforeCount + 1])
                    if i == 3:
                        stack.appendleft([currPoint[0],currPoint[1] + 1, currVal, beforeCount + 1])
        wayDict[point] = pointMax-1
        if pointMax > maxCount:
            maxCount = pointMax
        print(wayDict)
print(maxCount)
