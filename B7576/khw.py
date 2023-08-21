import sys
from collections import deque

input = sys.stdin.readline

# bfs 함수
def bfs(start: set, tomato_box: list):
    queue = deque()
    queue.append(start)
    count = 0
    while queue:
        this_turn = queue.popleft()
        next_turn = set()
        for i in this_turn:
            y = i[0]
            x = i[1]
            judge = False
            for j in range(4):
                new_y = y + dy[j]
                new_x = x + dx[j]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                    continue
                if tomato_box[new_y][new_x] == 0:
                    temp_count = count + 1
                    tomato_box[new_y][new_x] = temp_count
                    next_turn.add((new_y, new_x))
                    judge = True
        if judge:
            count += 1
        queue.append(next_turn)
    return tomato_box

m, n = map(int, input().split())
tomato = list(list(map(int, input().split())) for _ in range(n))
target = set()

# 1(토마토)의 좌표 찾기
for y in range(n):
    for x in range(m):
        if tomato[y][x] == 1:
            target.add((y,x))

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = bfs(target, tomato)

temp = set()
for i in answer:
    a = set(i)
    temp.union(a)

if 0 in temp:
    print(-1)
else:
    print(max(a))