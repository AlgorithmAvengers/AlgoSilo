import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
base = list(list(map(int, sys.stdin.readline().strip())) for _ in range(N))
# stride = 0
# for n in range(N):    
#     if sum(base[n]) > stride:
#         stride = sum(base[n])
# stride = min(stride, M, N)
stride = min(M, N) # M과 N 중에서 작은 것이 가능한 정사각형의 최대 길이

def rowCheck(row, col, stride, base):
    '''
    row에 대해서, 주어진 길이(stride)만큼 1이 있는지 확인하는 함수
    '''
    for i in range(stride):
        if base[row][col+i] != 1:
            return False
    return True

possSet = set() #가능한 숫자를 담아놓는 set
row, col = 0, 0

while stride > 1:
    if stride in possSet:
        break
    if base[row][col] == 1:
        for i in range(stride):
            if rowCheck(row+i, col, stride, base) == False: #한줄씩 내려가면서 체크함.
                possSet.add(i)
                break
        else:#stride만큼 다 문제없이 통과한 경우 -> 정사각형 만들어짐
            break
    col += 1 #이 자리는 틀렸으니 다음 자리로
    if col + stride - 1 >= M:
        row += 1
        col = 0
    if row + stride - 1 >= N:
        stride -= 1
        row = 0
        col = 0
print(stride**2)