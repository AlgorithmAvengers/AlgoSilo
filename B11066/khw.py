import sys

input = sys.stdin.readline

def djkim():
    # [i][k] + [k+1][j] + sum(i~j)
    for i in range(2, chapters+1): # 챕터 개수
        for j in range(1, chapters+2-i):   # 시작
            sheet[j][j+i-1] = min([sheet[j][j+k] + sheet[j+k+1][j+i-1] for k in range(i-1)]) + (sum_dict[j+i-1] - sum_dict[j-1])
 
    print(sheet[1][chapters])
 
for _ in range(int(input())):
    chapters = int(input())
    file_size = [0] + list(map(int, input().split()))
    sheet = [[0]*(chapters+1) for _ in range(chapters+1)]
    sum_dict = dict(zip(range(chapters+1), [0]*(chapters+1)))
    for i in range(1, chapters+1):
        sum_dict[i] = sum_dict[i-1] + file_size[i]
    djkim()


# # 순열 구현
# def permutation(arr: list):
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]

#     def generate(chosen, used):
#         if len(chosen) == len(arr):
#             return chosen

#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 chosen.pop()
#     generate([], used)

# for i in range(t):
#     all_case = permutation(file_size[i])
#     all_case_num = len(all_case)
    


# for i in range(t):
#     cost_list = [[0]*chapters[i] for _ in range(chapters[i])]
#     for a in range(chapters[i]):
#         for b in range(chapters[i]):
#             if a != b:
#                 cost_list[a][b] = file_size[i][a] + file_size[i][b]
#     # 플로이드 워셜 알고리즘
#     for j in range(chapters[i]):
#         for a in range(chapters[i]):
#             for b in range(chapters[i]):
#                 cost_list[a][b] = min(cost_list[a][b], cost_list[a][i]+cost_list[i][b])
    