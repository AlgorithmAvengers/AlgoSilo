import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
bamboo = []
for _ in range(n):
    bamboo.append(list(map(int, input().split())))
count_list = [[0]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def pandajump(x, y):
    if count_list[x][y] > 0:
        return count_list[x][y]
    count_list[x][y] = 1
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]
        if (0<=new_x<n) and (0<=new_y<n) and (bamboo[new_x][new_y]>bamboo[x][y]):
            count_list[x][y] = max(count_list[x][y], pandajump(new_x,new_y)+1)
    return count_list[x][y]

answer = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        answer[i][j] = pandajump(i, j)

final = max(map(max, answer))

print(final)