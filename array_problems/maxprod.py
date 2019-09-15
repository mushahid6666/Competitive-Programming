__author__ = 'mushahidalam'
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, arr):

        n = len(arr)

        # max positive product ending at the current position
        max_ending_here = 1

        # min positive product ending at the current position
        min_ending_here = 1

        # Initialize maximum so far
        max_so_far = 1

        # Traverse throughout the array_problems. Following values
        # are maintained after the ith iteration:
        # max_ending_here is always 1 or some positive product
        # ending with arr[i]
        # min_ending_here is always 1 or some negative product
        # ending with arr[i]
        for i in range(0, n):

            # If this element is positive, update max_ending_here.
            # Update min_ending_here only if min_ending_here is
            # negative
            if arr[i] > 0:
                max_ending_here = max_ending_here * arr[i]
                min_ending_here = min(min_ending_here * arr[i], 1)

            # If this element is 0, then the maximum product cannot
            # end here, make both max_ending_here and min_ending_here 0
            # Assumption: Output is alway greater than or equal to 1.
            elif arr[i] == 0:
                max_ending_here = 1
                min_ending_here = 1

            # If element is negative. This is tricky
            # max_ending_here can either be 1 or positive.
            # min_ending_here can either be 1 or negative.
            # next min_ending_here will always be prev.
            # max_ending_here * arr[i]
            # next max_ending_here will be 1 if prev
            # min_ending_here is 1, otherwise
            # next max_ending_here will be prev min_ending_here * arr[i]
            else:
                temp = max_ending_here
                max_ending_here = max(min_ending_here * arr[i], 1)
                min_ending_here = temp * arr[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
        if anyOne:
            return max_so_far
        else:
            return 0

        return max_so_far

A = Solution()
B = [2,-1, 2,-4,-1,4]
print A.maxProduct(B)
