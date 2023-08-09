class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # k가 1일 경우에는 나눌 수 없으므로 반드시 차이가 0
        # weights가 2인 경우에는 max와 min이 동일하므로 차이가 0
        if k == 1 or len(weights) == 2:
            return 0
        
        # 서로 인접한 것들끼리 더해지므로 인접한 것들을 더한 것을 바탕으로 비교
        n = len(weights)
        pair_weights = [0] * (n - 1)
        for i in range(n - 1):
            pair_weights[i] = weights[i] + weights[i + 1]
        pair_weights.sort()
        
        answer = 0
        for i in range(k - 1):
            answer += pair_weights[n - 2 - i] - pair_weights[i]
            
        return answer