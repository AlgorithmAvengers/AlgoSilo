import sys
from collections import deque

# 뒤집어주는 함수 선언
def R():
    if isR == True:
        return False
    else:
        return True

# 앞에 있는 원소 하나 삭제하는 함수 선언
def D(lst):
    if isR == False:
        lst.popleft()
    else:
        lst.pop()

# 전체 test case 갯수 input 받기
input = sys.stdin.readline

T = int(input())

# 각각의 T번만큼 출력값을 내놓기 위한 for문 시작
for t in range(T):
    # 전체 input 받기
    function = input().strip()
    n = int(input())

    # list를 뒤집을지 말지 결정하는 변수
    isR = False

    # error 여부를 판단하는 변수
    isE = False

    # input 받기
    num = deque(input().strip()[1:-1].split(','))

    # ''도 하나의 원소로 포함하게 되므로, 길이가 0일 경우에 []로 초기화하는 것이 필요함
    if n == 0:
        num = []

    # 'R'일 경우와 'D'일 경우 케이스를 나누어서 처리   
    for i in range(len(function)):
        if function[i] == "R":
            isR = R()
        else:
            if len(num) == 0:
                isE = True
                break
            else:
                D(num)

    # error라는 것이 판명되면, 뒤에 출력으로 넘어가지 않고 바로 'error' 출력
    if isE == True:
        print('error')
    else:
        if isR == True:
            num.reverse()
            print('[' + ",".join(num) + ']')
        else:
            print('[' + ",".join(num) + ']')