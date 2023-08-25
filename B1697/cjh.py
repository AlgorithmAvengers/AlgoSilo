from collections import deque
import sys

subin, sister = map(int, sys.stdin.readline().rstrip().split())
max_num = 100000
visited = [0] * (max_num + 1)

def BFS():
    queue = deque([subin])

    while queue:
        t = queue.popleft()

        if t == sister:
            print(visited[t])
            break
        
        for i in (t-1, t+1, t*2):
            if 0 <= i <= max_num and not visited[i]:
                visited[i] = visited[t] + 1
                queue.append(i)

BFS()