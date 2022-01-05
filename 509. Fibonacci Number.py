class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        a = 0
        b = 1
        for i in range(n-1):
            a, b = b, a+b
        return b