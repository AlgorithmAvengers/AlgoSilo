class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = 1
        nums.sort()
        for i in nums:
            if i == temp:
                temp += 1

        return temp