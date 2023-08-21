class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] * nums[1] + max(nums)
        else:
            alist = []
            for i in range(len(nums)):
                temp = nums.copy()
                if i > 0 and i < len(nums)-1:
                    score = temp[i-1] * temp[i] * temp[i+1]                    
                elif i == 0:
                    score = temp[i] * temp[i+1]
                else:
                    score = temp[i-1] * temp[i]
                temp.pop(i)
                alist.append(score + self.maxCoins(temp))
            return max(alist)
        