class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n%3==0:
            return self.isPowerOfThree(n//3)
        if n==1:
            return n==1
        return False
        