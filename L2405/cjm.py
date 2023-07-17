class Solution:
    def partitionString(self, s: str) -> int:
        split = 0
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                split += 1
                count = {s[i]:1}
            else:
                count[s[i]] = 1
        return split+1

class Solution:
    def partitionString(self, s: str) -> int:
        split = 1
        count = {}
        for i in s:
            if i in count:
                split += 1
                count = {i:1}
            else:
                count[i] = 1
        return split
    
class Solution:
    def partitionString(self, s: str) -> int:
        split = 1
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                split += 1
                count = {s[i]:1}
            else:
                count[s[i]] = 1
        return split