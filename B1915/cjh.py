n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().rstrip))))

result = 0
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = graph[i][j]
        elif graph[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        result = max(dp[i][j], result)

print(result * result)