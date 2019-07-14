class Solution:
    def fib(self, N):
        a = 0
        b = 1
        for i in range(N):
            yield a
            a,b = b,a+b






