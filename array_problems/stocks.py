__author__ = 'mushahidalam'

    import sys
    class Solution:
        # @param A : tuple of integers
        # @return an integer
        def maxProfit(self, A):
            if len(A) == 0:
                return 0
            if len(A) == 1:
                return 0
            min_element = sys.maxint
            max_profit = -sys.maxint
            min_element_index = -1
            max_element_index= -1
            for i in range(len(A)):
                if A[i] < min_element:
                    min_element = A[i]
                    min_element_index = i
                if max_profit < A[i] - min_element:
                    max_profit = A[i] - min_element
                    max_element_index = i

            if max_profit == -sys.maxint:
                return [0,0]
            return [min_element_index, max_element_index]

        # C Solution
        # int maxProfit(const int* A, int n1) {
        #     int max_diff = A[1] - A[0];
        #       int min_element = A[0];
        #       int i;
        #       for(i = 1; i < n1; i++)
        #       {
        #         if (A[i] - min_element > max_diff)
        #           max_diff = A[i] - min_element;
        #         if (A[i] < min_element)
        #              min_element = A[i];
        #       }
        #       if(max_diff < 0) return 0;
        #       return max_diff;
        # }

obj = Solution()
prices = [1,2,3,4,5]
print obj.maxProfit(prices)