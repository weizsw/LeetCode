class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizz_buzz = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                fizz_buzz.append('FizzBuzz')
            elif num % 3 == 0:
                fizz_buzz.append('Fizz')
            elif num % 5 == 0:
                fizz_buzz.append('Buzz')
            else:
                fizz_buzz.append(str(num))
        return fizz_buzz