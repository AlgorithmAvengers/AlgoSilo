"""
추의 갯수 = w_num
추의 무게 리스트 = weights

구슬의 갯수 = m_num
구슬의 무게 리스트 = marbles
"""
w_num = int(input())
weights = list(map(int, input().split()))

m_num = int(input())
marbles = list(map(int, input().split()))

"""
DP 행렬 초기화해주기
추의 최대 무게만큼의 길이의 행렬을 생성하는데 
추의 무게가 500g 이하이므로 501까지 range로 열을 만들어주면 됨
그리고 추의 무게의 갯수만큼의 행을 가지게 됨
"""
dp = [[0 for j in range((i+1)*500+1)] for i in range(w_num+1)]

result = []

# DP라는 함수를 통하여 dp 행렬을 채울 수 있도록 함(gram는 추로 나타낼 수 있는 무게, weight은 추의 무게를 나타냄)
def DP(gram, weight):
    # gram이 w_num보다 큰 경우에는 dp에 저장 가능한 무게가 아니므로 return
    if gram > w_num:
        return
    
    # 이미 나타낼 수 있는 무게라면 return
    if dp[gram][weight]:
        return
    
    # 위의 두 경우를 모두 통과하면 가능한 무게로 고려함
    dp[gram][weight] = 1

    # 추를 구슬과 함께 놓을지, 아니면 다른 곳에 놓을지 아예 올리지 않을지 기준으로 나누어서 각각의 함수를 호출
    DP(gram+1, weight)
    DP(gram+1, weight + weights[gram-1])
    DP(gram+1, abs(weight - weights[gram-1]))

# 시작점으로부터 전체 dp 행렬을 채우는 함수를 실행함
DP(0, 0)

for i in marbles:
    # 추가 30개의 이상이거나, 500g이 넘는 경우는 불가능하므로, 해당 경우의 edge case 고려 필요
    if i > 30*500:
        result.append('N')
        continue

    elif dp[w_num][i] == 1:
        result.append('Y')
    else:
        result.append('N')

# 리스트 안의 원소들만 출력해줄 수 있도록 함
print(*result)