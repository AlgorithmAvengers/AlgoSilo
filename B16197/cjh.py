import sys

input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
# initialization
n, m = map(int, input().split())
visited = [[-1 for _ in range(n)] for _ in range(m)]

def __DFTHELP(r: int, c: int, step: int)-> None:
    # Complete __DFTHELP function for DFT recursion #
    if r==0 and c==0:
        visited[r][c]=0
    for d in range(4):
        if (r+dr[d]<0) or (c+dc[d]<0) or (r+dr[d]>=M) or (c+dc[d]>=N):
            continue
            if field[r+dr[d]][c+dc[d]] != -1:
                if (visited[r+dr[d]][c+dc[d]] == -1) or (visited[r+dr[d]][c+dc[d]] > step+1):
                    visited[r+dr[d]][c+dc[d]] = step+1
                    __DFTHELP(r+dr[d],c+dc[d], step+1)
def DFT():
    __DFTHELP(0, 0, 0)
    ans = DFT()
    for i in range(M):
        for j in range(N):
            if field[i][j]=='':
                ans = visited[i][j]
    return ans

board = []
tmp = []
for i in range(n):
        board.append(list(input().strip()))
        for j in range(m):
            if board[i][j] == "o":
                tmp.append((i, j))