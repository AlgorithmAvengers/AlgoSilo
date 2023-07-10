class Solution:
    def findNthDigit(self, n: int) -> int:
        result = ''
        ans = 9
        save = 0
        i = 1
        while True:
            if n <= ans:
                interval = (n-save) // i
                mod = (n-save) % i
                if mod == 0:
                    return int(str(10**(i-1) + interval-1)[-1])
                if mod != 0:
                    return int(str(10**(i-1)+interval)[mod-1])
            else:
                i += 1
                save = ans
                ans += i * 9*(10**(i-1))
