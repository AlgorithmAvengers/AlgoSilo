class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # k가 1일 경우에는 나눌 수 없으므로 반드시 차이가 0
        # weights가 2인 경우에는 max와 min이 동일하므로 차이가 0
        if k == 1 or len(weights) == 2:
            return 0
        
        # 나머지의 경우에 k-1개 만큼의 분할선을 가진다고 가정하고 문제를 풀 수 있음
        from itertools import combinations
        lines = [i+1 for i in range(len(weights)-1)]
        combi = list(combinations(lines, k-1))

        MaxScore = 0
        MinScore = 99999999
        for i in range(len(combi)):
            start = 0
            total = 0
            for j in range(len(combi[0])):
                end = combi[i][j]
                total += weights[start]
                total += weights[end-1]
                start = end
            total += weights[end]
            total += weights[-1]

            if total < MinScore:
                MinScore = total
            if total > MaxScore:
                MaxScore = total

        return MaxScore - MinScore