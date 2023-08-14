import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = list(list(map(int, list(input().strip()))) for _ in range(n))
sheet = list([0]*m for _ in range(n))

def check(pt1, pt2):
    # 모서리는 어차피 정사각형 안 나옴
    if pt1 == 0 or pt2 == 0:
        return 1
    else:
        return min(sheet[pt1-1][pt2-1], sheet[pt1-1][pt2], sheet[pt1][pt2-1]) + 1

answer = 0

for i in range(n):
    for j in range(m):
        # 0은 취급 안 함
        if board[i][j] == 1:
            sheet[i][j] = check(i,j)
            # 비교하여 최대치가 정답
            answer = max(answer, sheet[i][j])

print(answer**2)