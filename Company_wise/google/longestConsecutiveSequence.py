"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
100
4 3-4
200
1 -2
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set()
        for i in range(len(nums)):
            nums_set.add(nums[i])

        longest_sequence = 0
        for i in range(len(nums)):
            digit = nums[i]
            if digit -1 not in nums_set:
                cur_seq = 1
                while digit +1  in nums_set:
                    cur_seq += 1
                    digit  = digit +1
                longest_sequence = max(longest_sequence, cur_seq)
        return longest_sequence

obj = Solution()
nums = [100, 4, 200, 1, 3, 2]
nums = [1,2,0,1]

print obj.longestConsecutive(nums)