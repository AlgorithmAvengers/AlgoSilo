import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def binary_search(time = list(), left = int(), right = int(), n = int(), m = int(), result = int()):
    if left > right:
        return None
    mid = (left+right)//2
    total = 0
    for i in range(m):
        total += mid//time[i]
    if (total >= m):
        result = min(result, mid)
        return binary_search(time = time, left = left, right = mid + 1, n = n, m = m, result = result)
    else:
        return binary_search(time = time, left = mid - 1, right = right, n = n, m = m, result = result)

n, m = map(int, input().split())
time = []
for _ in range(n):
    time.append(int(input()))

result = max(time) * m

binary_search(time = time, left = min(time), right = result, n = n, m = m, result = result)

print(result)