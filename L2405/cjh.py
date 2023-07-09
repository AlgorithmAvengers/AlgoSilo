class Solution:
    def partitionString(self, s: str) -> int:
        num = 1
        length = 0

        temp = set()
        for i in range(len(s)):
            if len(s) > 1 and i == 0:
                if s[i] == s[i+1]:
                    num += 1
                    pass
                else:
                    temp.add(s[i])
                    length += 1
            else:
                temp.add(s[i])
                length += 1
                if len(temp) < length:
                    num += 1
                    temp = set()
                    temp.add(s[i])
                    length = 1
                else:
                    continue
        return num