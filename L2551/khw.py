class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # k =1이면 무조건 0
        if k == 1:
            return 0

        # 칸막이 리스트를 생성하여
        kanmagi = []
        # 두 개씩 묶어 합하고
        for i in range(1, len(weights)):
            kanmagi.append(weights[i-1]+weights[i])
        # 정렬 하여
        kanmagi.sort()
        # 앞 k-1, 뒤 k-1 차이
        return sum(kanmagi[-k+1:])-sum(kanmagi[:k-1])
