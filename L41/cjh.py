class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        from collections import deque
        min_int = 1
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == min_int:
                min_int += 1
        return min_int