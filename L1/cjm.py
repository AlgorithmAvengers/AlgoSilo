class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {nums[0]:0}
        for i in range(1, len(nums)):
            diff = target - nums[i]
            if diff in check:
                return [check[diff], i]
            else:
                check[nums[i]] = i