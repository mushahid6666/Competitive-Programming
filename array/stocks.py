__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 0
        min_element = A[0]
        max_so_far = A[1] - A[0]
        for i in range(1, len(A)):
            if A[i] - min_element > max_so_far:
                max_so_far = A[i] - min_element
            if A[i] < min_element:
                min_element = A[i]
        if max_so_far < 0:
            return 0
        return max_so_far

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
