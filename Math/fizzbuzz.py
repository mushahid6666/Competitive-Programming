class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
                continue
            elif i % 3 == 0:
                result.append("Fizz")
                continue
            elif i % 5 == 0:
                result.append("Buzz")
                continue
            else:
                result.append(str(i))
                continue
        return result

obj = Solution()
print obj.fizzBuzz(15)


