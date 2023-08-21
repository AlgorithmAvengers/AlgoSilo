n = int(input())

for i in range(n):
    l = int(input())
    text = list(map(int, input().split()))

    dp = [[0] * l for _ in range(l)]

    for i in range(l-1):
        dp[i][i+1] = text[i] + text[i+1]
        for j in range(i+2, l):
            dp[i][j] = dp[i][j-1] + text[j]

    for d in range(2, l):
        for i in range(l-d):
            j = i + d
            minimum = [dp[i][s] + dp[s+1][j] for s in range(i, j)]
            dp[i][j] += min(minimum)

    print(dp[0][l-1])