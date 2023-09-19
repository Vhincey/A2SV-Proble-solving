class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1:
            return True
        elif n < 1:
            return False
        elif n % 4 != 0:
            return False
        return self.isPowerOfFour(n // 4)

        # if n == 1:
        #     return True

        # if n <= 0:
        #     return False

        # while n % 4 == 0:
        #     n //= 4
       
        # return n == 1

        

       
