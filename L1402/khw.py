class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        a = []
        thesum = 0
        for i in range(len(satisfaction)+1):
            for j in range(i):
                thesum += satisfaction[j]*(i-j)
            a.append(thesum)
            thesum = 0
        return max(a)