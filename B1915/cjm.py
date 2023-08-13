import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
base = list(list(map(int, sys.stdin.readline().strip())) for _ in range(N))
# big = 0
# for n in range(N):    
#     if sum(base[n]) > big:
#         big = sum(base[n])
# big = min(big, M, N)
big = min(M, N)

def rowCheck(row, col, big, base):
    for i in range(big):
        if base[row][col+i] != 1:
            return False
    return True

possSet = set()
row, col = 0, 0

while big > 1:
    if big in possSet:
        break
    if base[row][col] == 1:
        for i in range(big):
            if rowCheck(row+i, col, big, base) == False:
                possSet.add(i)
                break
        else:
            break
    col += 1
    if col + big - 1 >= M:
        row += 1
        col = 0
    if row + big - 1 >= N:
        big -= 1
        row = 0
        col = 0
print(big**2)