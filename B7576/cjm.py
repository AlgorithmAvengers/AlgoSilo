import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split())  #열, 행

container = [] #기본 보관함

for row in range(N):
    container.append(list(map(int, sys.stdin.readline().strip().split())))

epMax = 9999999 #무한대 대용
DP = [[epMax]*M for _ in range(N)] #모두 무한대로 채워놓음
BFS = deque()
maxNum = N * M #아직 체크 못한 토마토 숫자
startPoint = []
for row in range(N):
    for col in range(M):
        if container[row][col] == 1:
            BFS.append(((row, col), 0))
            maxNum -= 1
            DP[row][col] = 1
        elif container[row][col] == -1:
            DP[row][col] = -1
            maxNum -= 1

def check(dummy):
    '''
    dummy 변수는 이중 tuple로 ((행, 열), 이전 거리)로 구성됨.
    udlr : up, down, left, right
    '''
    global maxNum
    point = dummy[0]
    val = dummy[1]
    udlr = [(point[0]-1,point[1]), (point[0]+1, point[1]), (point[0], point[1]-1), (point[0], point[1]+1)]
    for row, col in udlr:
        if row < 0 or col < 0 or row >= N or col >= M: #index가 벗어나는 경우
            continue
        if container[row][col] == 0: #index가 벗어나지 않고, container에서의 값이 0인 경우(빈 공간:-1 예외처리)
            if DP[row][col] > val+1: #DP행렬의 값보다 val+1이 작은 경우만
                if DP[row][col] == epMax: #맨 처음 들린 경우, maxNum에서 1을 빼서 남은 숫자 관리해줌
                    maxNum -= 1
                DP[row][col] = val+1
                BFS.append(((row, col), val+1))

            

while BFS.__len__() > 0:
    temp = BFS.popleft()
    check(temp)

if maxNum > 0:
    print(-1)
else:
    print(temp[1])