import sys

input = sys.stdin.readline

n = int(input())
bd = list(map(int, input().split()))
count_list = []

if n == 1:
    print(0)
    exit()
elif n == 2:
    print(1)
    exit()
elif n == 3:
    print(2)
    exit()
else: # 일반적인 경우
    for i in range(n):# i는 기준점
        count = 0
        if i == 0:# 첫 번째 건물
            for j in range(1,n):
                slope = (bd[j]-bd[0])/j
                score = 1
                for l in range(1,j):
                    if bd[l]>=(slope*(l-i)+bd[i]):
                        score = 0
                        break
                count = count + score
            count_list.append(count)
        elif i == n-1:# 마지막 건물
            for j in range(i-1,-1,-1):
                slope = (bd[i]-bd[j])/(i-j)
                score = 1
                for l in range(i-1,j,-1):
                    if bd[l]>=(slope*(l-i)+bd[i]):
                        score = 0
                        break
                count = count + score
            count_list.append(count)
        else:# 일반적인 경우
            for j in range(i-1,-1,-1):# i건물 기준으로 그 앞의 건물들에 대해 기준 만족 여부 검토
                slope = (bd[i]-bd[j])/(i-j)
                score = 1
                for l in range(i-1,j,-1):
                    if bd[l]>=(slope*(l-i)+bd[i]):# 만약 미충족 시 그 건물은 노 카운트
                        score = 0
                        break
                count = count + score# 충족 시 카운트
            for j in range(i+1,n):# i건물 기준 그 뒤의 건물들에 대해 기준 만족 여부 검토
                slope = (bd[j]-bd[i])/(j-i)
                score = 1
                for l in range(i+1,j):
                    if bd[l]>=(slope*(l-i)+bd[i]):
                        score = 0
                        break
                count = count + score
            count_list.append(count)# 최종 스코어를 카운트 리스트에 기록

    print(max(count_list))

