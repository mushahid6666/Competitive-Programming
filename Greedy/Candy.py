__author__ = 'mushahidalam'


#
# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following
# requirements:Each child must have at least one candy.Children with a higher
#  rating get more candies than their neighbors.What is the minimum candies you must give?
class Solution:
    # @param ratings : list of integers
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        candies = [0] * n
        candies[0] = 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            else:
                candies[i] = 1
        result = candies[n - 1]
        for i in range(n - 2, -1, -1):
            cur = 1
            if ratings[i] > ratings[i + 1]:
                cur = candies[i + 1] + 1
            result += max(cur, candies[i])
            candies[i] = cur
        return result


obj = Solution()
ratings = [3, 2, 1]
print obj.candy(ratings)
