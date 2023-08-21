class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # balloons 양 옆에 [1]이라는 padding 넣어주기(인덱스가 끝까지 가면 1을 곱해주기로 했기 때문)
        balloons = [1] + nums + [1]

        # balloons의 길이를 측정하여 추후 loop에 용이하게 사용
        n = len(balloons)

        # dp 행렬을 만들어서 초기화 해줌
        dp = [[0] * n for _ in range(n)]

        """
        i가 n-2부터 시작하는 것은 기존의 nums까지만 보기 위해서
        뒤에서부터 거꾸로 확인하면서 nums 앞까지 dp 행렬을 채우게 됨
        근데 k가 왜 필요한 것이 지금까지의 max값을 찾기 위해서인지 잘 이해하지 못하겠음...
        """
        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], balloons[i] * balloons[k] * balloons[j] + dp[i][k] + dp[k][j])

        # 가장 맨 앞에까지 오면서 가장 큰 값을 저장하므로, 그런데 왜 [0][n-1]을 return 해야하는 것이지...?
        return dp[0][n-1]