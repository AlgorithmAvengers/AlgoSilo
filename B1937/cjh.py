# input 저장
n = int(input())

# 대나무밭 maps input 저장
maps = []
# maps의 숫자를 개별적으로 저장
numbers = []
for i in range(n):
    a = list(input())
    maps.append(a)
    for j in range(len(a)):
        numbers.append((a[j], i, j))

result = []
# DFS 함수 먼저 작성
from collections import deque
def dfs(number):
    visited = []
    temp = 0
    stack = [number]
    while stack:
        if temp <= n:
            node = stack.pop()
        if node not in visited:
            visited.append(node)
            for dx,dy in direction:
                bamboo, x, y = node
                if 0 <= x + dx < len(maps[0]) and 0 <= y + dy < len(maps):
                    nx = x + dx
                    ny = y + dy
                    if maps[nx][ny] > bamboo:
                        stack.append(node)
                        temp += 1
        result.append(temp)
    return result

# numbers를 오름차순으로 정렬
numbers = sorted(numbers)

# 가장 작은 값부터 dfs를 할 수 있도록 함
direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for number in numbers:
    dfs(number)

print(max(result))