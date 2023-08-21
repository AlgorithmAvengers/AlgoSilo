class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return nums[0]*nums[1] + max(nums[0],nums[1])
        else:
            nums.insert(0,1)
            nums.append(1)
            sheet = [[0]*(n + 2) for _ in range(n + 2)]

            for size in range(n):
                limit = n - size + 1
                for start in range(1, limit):
                    end = start + size
                    for i in range(start, end + 1):
                        this_turn = sheet[start][i-1] + sheet[i+1][end] + nums[start-1]*nums[i]*nums[end+1]
                        sheet[start][end] = max(sheet[start][end], this_turn)

            return sheet[1][n]