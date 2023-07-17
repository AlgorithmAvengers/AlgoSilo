class Solution:
    def findNthDigit(self, n: int) -> int:
        my_digit = 1
        temp = 9

        while n > my_digit*temp:
            n -= my_digit*temp
            my_digit += 1
            temp *= 10
        
        starting = 10 ** (my_digit-1)

        a = (n-1)//my_digit
        b = (n-1)%my_digit
        c = starting + a

        return int(str(c)[b])