class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sNums = set(nums)
        for i in range(1, len(sNums)+1):#그냥 1부터 찾아보기 음수가 있으면 그 전에 끝날거니까.
            if i not in sNums:
                return i
        else:
            return len(sNums)+1 #문제없었으면 다 양수고, 다 있는거니까 마지막+1