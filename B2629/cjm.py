import sys

N = int(sys.stdin.readline().strip())  # 추 개수
chooList = list(map(int, sys.stdin.readline().strip().split())) # 추 목록

M = int(sys.stdin.readline().strip()) # 구슬 개수
marbleList = list(map(int, sys.stdin.readline().strip().split())) #구슬 목록
weightSet = set()
chooIdx = 0
marbleIdx = 0
cal = [-1,0,1]
ans = ""
while marbleIdx < M:
    while chooIdx < N:
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
    else:
        if marbleList[marbleIdx] not in weightSet:
            ans += 'N '
        else:
            ans += "Y "
        marbleIdx += 1
print(ans.strip())