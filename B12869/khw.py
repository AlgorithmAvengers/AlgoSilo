import sys
input = sys.stdin.readline

n = int(input())

scv = list(map(int, input().split()))
# k=1, k=2일 경우 대비
scv.extend([0, 0])

# 모든 경우의 수에 대해 [x][y][z]의 count를 기록
dp = [[[0]*61 for _ in range(61)] for _ in range(61)]
# scv들의 현재 체력은 count 1로 설정
dp[scv[0]][scv[1]][scv[2]] = 1

# 가능한 공격 패턴
combi = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            # 모든 경우의 수들에 대해 for loop
            if dp[i][j][k] > 0:
                # 공격 패턴들
                for c in combi:
                    i_ = i-c[0] if i-c[0] >= 0 else 0
                    j_ = j-c[1] if j-c[1] >= 0 else 0
                    k_ = k-c[2] if k-c[2] >= 0 else 0
                    # 처음 도착한 경우 or 더 적은 횟수로 도착하는 경우에만 업데이트
                    if dp[i_][j_][k_] == 0 or dp[i_][j_][k_] > dp[i][j][k]+1:
                        dp[i_][j_][k_] = dp[i][j][k]+1

print(dp[0][0][0]-1)

