import numpy as np

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        idx = -1
        for i in range(len(satisfaction)):
            if satisfaction[i] >= 0:
                idx = i
                break
        if idx == -1:
            return 0
        while True:
            ar_sat = np.array(satisfaction[idx:])
            result = np.sum(ar_sat * np.arange(1, len(ar_sat)+1))
            if np.sum(ar_sat) + satisfaction[idx-1] < 0 or idx <= 0:
                return result
            idx -= 1

            
            
        return result