class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        coins = 0

        nums_dict = dict()
        for i in range(n-2):
            nums_dict[i+1] = nums[i+1]
        
        nums_dict = sorted(nums_dict.items(), key = lambda item: item[1])

        print(nums_dict)

        for i in range(len(nums_dict)):
            index = nums_dict[i][0]
            print(index)
            temp = nums[index-1] * nums[index] * nums[index+1]
            coins += temp
            del nums[index]

        print(nums)