class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        time = [i+1 for i in range(len(satisfaction))]
        sorted_sat = sorted(satisfaction)

        del_num = 0
        for i in range(len(sorted_sat)):
            if sorted_sat[i]+sum(sorted_sat[i+1:]) < 0:
                del_num += 1
        sorted_sat = sorted_sat[del_num:]

        result = 0
        for j in range(len(sorted_sat)):
            result += time[j] * sorted_sat[j]

        return result