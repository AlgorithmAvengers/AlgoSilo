import sys
input = sys.stdin.readline

n = int(input())
bamboo = []
for _ in range(n):
    bamboo.append(list(map(int, input().split())))
count_list = [[0]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def pandajump(x, y):
    if count_list[x][y] > 0:
        return count_list[x][y] - 1
    count_list[x][y] = 1
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dx[i]
        if 0<=new_x<n and 0<=new_y<n and bamboo[new_y][new_x]>bamboo[y][x]:
            count_list[x][y] += pandajump(new_x,new_y)
    return count_list[x][y]

answer = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        answer[i][j] = pandajump(i, j)

final = max(map(max, answer))

print(final)