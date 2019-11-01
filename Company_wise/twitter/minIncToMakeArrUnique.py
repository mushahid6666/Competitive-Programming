import collections
class Solution(object):
    def minIncrementForUnique1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

    def minIncrementForUnique2(self, A):
        if len(A) == 0 or len(A) == 1:
            return 0
        num_range = [0] * 40000
        num_moves = 0
        for i in range(len(A)):
            num_range[A[i]] += 1
        for i in range(len(A)):
            cur_num = A[i]
            if num_range[cur_num] > 1:
                num_range[cur_num] -=1
                cur_num += 1
                num_moves += 1
                while num_range[cur_num] >= 1:
                    cur_num += 1
                    num_moves += 1
                num_range[cur_num] = 1
        return num_moves


    def minIncrementForUnique1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0 or len(A) == 1:
            return 0

        num_map = collections.defaultdict(int)
        for i in range(len(A)):
            num_map[A[i]] += 1
        total_moves = 0
        for i in range(len(A)):
            cur_num = A[i]
            cur_count = num_map[cur_num]
            if cur_count > 1:
                num_map[cur_num] -= 1
                cur_num += 1
                total_moves += 1
                while cur_num in num_map:
                    cur_num += 1
                    total_moves += 1
                num_map[cur_num] = 1
        return total_moves




obj = Solution()
Input= [1,2,2]
print obj.minIncrementForUnique(Input), ": 1"

Input= [3,2,1,2,1,7]

print obj.minIncrementForUnique(Input), ": 6"

