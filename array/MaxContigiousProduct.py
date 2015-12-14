__author__ = 'mushahidalam'
__author__ = 'mushahidalam'


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        prev_max_prod = A[0]
        prev_min_prod = A[0]
        max_so_far = A[0]

        for i in range(1, len(A)):
            temp = prev_max_prod
            prev_max_prod = max(max(A[i] * prev_max_prod, A[i]), A[i] * prev_min_prod)
            prev_min_prod = min(min(A[i] * temp, A[i]), A[i] * prev_min_prod)
            max_so_far = max(max_so_far, prev_max_prod)
        return max_so_far


A = Solution()
B = [0, -1, 0, -4, -1, 0]
print A.maxProduct(B)
