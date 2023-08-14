import sys
'''
추 2개로 만들 수 있는 경우의 수 : 추1 + 추2, 추1 - 추2, 추1 + 0*추2, 0*추1+추2
그 다음에 추가 1개 추가되면, 그 이전 목록의 모든 값들과 다시 계산해주면 됨
'''
N = int(sys.stdin.readline().strip())  # 추 개수
chooList = list(map(int, sys.stdin.readline().strip().split())) # 추 목록

M = int(sys.stdin.readline().strip()) # 구슬 개수
marbleList = list(map(int, sys.stdin.readline().strip().split())) #구슬 목록
weightSet = set() #만들 수 있는 무게 목록
chooIdx = 0
marbleIdx = 0
cal = [-1,0,1] # 계산의 편의를 위한 list : 
ans = ""
while marbleIdx < M: # 주어진 구슬들 다 계산할 때까지
    while chooIdx < N: # 주어진 추 다 계산할 때까지
        if len(weightSet) == 0:
            weightSet.add(chooList[chooIdx])
        else:
            tempList = []
            for weight in weightSet:
                for i in range(3):
                    for j in range(3):
                        tempList.append(abs(weight * cal[i] + chooList[chooIdx] * cal[j]))
            weightSet = set(tempList) | weightSet
        chooIdx += 1
        if marbleList[marbleIdx] in weightSet:
            ans += 'Y '
            marbleIdx += 1
            break
    else: #주어진 추를 다 썼는데도 구슬 계산이 안 된 경우
        if marbleList[marbleIdx] not in weightSet:
            ans += 'N '
        else:
            ans += "Y "
        marbleIdx += 1
print(ans.strip())