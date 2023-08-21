from collections import deque

n, m = map(int, input().split())
tomato = []

for i in range(m):
    temp = list(map(int, input().split()))
    tomato.append(temp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < m and 0 <= ny < n and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])

queue = deque()

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append([i, j])

bfs()

res = 0
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
    res = max(res, max(tomato[i]))

# 처음에 익은 토마토가 1이었으므로 1을 빼주어야 함
print(res - 1)
