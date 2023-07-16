import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([SG_x, SG_y])
    visited[0] = True
    while q:
        x, y = q.popleft()
        if ((abs(x-F_x)+abs(y-F_y))//50) <= 20:
            print('happy')
            return
        for i in range(n+1):
            temp_x, temp_y = graph[i]
            if visited[i] == False & ((abs(x-temp_x) + abs(y-temp_y))//50) <= 20:
                visited[i] = True
                q.append([temp_x, temp_y])
    print('sad')
    return

t = int(input())

for _ in range(t):
    n = int(input())
    SG_x, SG_y = map(int, input().split())
    graph = [[SG_x, SG_y]]
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append([x,y])
    F_x, F_y = map(int, input().split())
    visited = [False] * (n+1)
    bfs()