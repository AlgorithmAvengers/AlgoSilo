class Solution:
    def partitionString(self, s: str) -> int:
        a = []
        temp = ""
        for i in range(len(s)):
            tempchr = s[i]
            if temp.find(tempchr) == -1:
                temp = temp + tempchr
            else:
                a.append(temp)
                temp = tempchr
        return len(a) + 1