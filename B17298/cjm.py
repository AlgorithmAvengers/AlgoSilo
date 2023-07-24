import sys
from collections import deque


N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
ansDict = {}
for i in range(N):
    ansDict[i] = -1
check = deque()
check.
check.appendleft(0)
checksize = 1
for i in range(1, N):
    while checksize > 0 and array[check.popleft()] < array[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

    if array[temp] < array[i]:
        ansDict[temp] = array[i]
    else:
        check.appendleft(temp)
    check.appendleft(i)
# count = 1
# while count < N:
#     cpr = array[count]
#     while checksize > 0:
#         temp = check.popleft()
#         checksize -= 1
#         if temp < cpr:
#             ansDict[temp] = cpr
#             if checksize == 0:
#                 check.appendleft(cpr)
#                 checksize += 1
#                 break

#         else:
#             check.appendleft(temp)
#             check.appendleft(cpr)
#             checksize += 2
#             break
        
#     count += 1

print(' '.join(list(map(str, ansDict.values()))))

