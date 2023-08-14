class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        small = 99999999
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] < small:
                small = nums[i]
        if small > 1:
            return 1
        else:
            while True:
                for i in range(len(nums)):
                    if nums[i] == small + 1:
                        small += 1
                else:
                    return small + 1