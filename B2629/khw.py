import sys

input = sys.stdin.readline

weight_num = int(input())
weight_list = list(map(int,input().split()))

bead_num = int(input())
bead_list = list(map(int,input().split()))

sheet = {i:False for i in range(sum(weight_list)+1)}
sheet[0] = True

# 추의 무게의 합 전부 구해서 sheet에 기록
for w in weight_list:
    for weight_sum, TorF in list(sheet.items()):
        if TorF:
            if not sheet[weight_sum+w]:
                sheet[weight_sum+w] = True

# 모든 무게에서 추를 구슬 쪽에 올려 sheet에 기록
for w in weight_list:
    for weight_sum, TorF in list(sheet.items()):
        if TorF:
            if weight_sum - w >= 0 and ~(sheet[weight_sum - w]):
                sheet[weight_sum - w] = True

for b in bead_list:
    if b > sum(weight_list):
        print("N", end= " ")
        continue
    if sheet[b]:
        print("Y", end=" ")
    else:
        print("N", end=" ")