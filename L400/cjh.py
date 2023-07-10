class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        else:
            digits = 1
            while n > digits * 10 ** digits:
                n -= digits * (9 * 10**(digits-1))
                digits += 1
            target = 10 ** (digits - 1) + (n - 1)//digits
            idx = (n-1) % digits
        return int(str(target)[idx])