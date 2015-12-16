__author__ = 'mushahidalam'


class Solution:
    # momoized version
    def fibonacci(self, n):
        fib = {}
        for k in range(1, n + 1):
            if k <= 2:
                f = 1
            else:
                f = fib[k - 1] + fib[k - 2]
            fib[k] = f
        return fib[n - 1]


A = Solution()
print(A.fibonacci(4))
