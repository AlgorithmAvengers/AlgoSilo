import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = []
for i in range(n):
    time.append(int(input()))

time.sort()

start = time[0]
end = time[-1] * m # 최대 시간*인원수

# 최소값을 찾기 위해 먼저 result는 end로 initialize
result = end
while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in range(n):
        total += mid // time[i]

    if total < m:
        start = mid + 1
    else:
        end = mid - 1
        result = min(result, mid)

print(result)