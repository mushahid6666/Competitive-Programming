# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = m - 1
        k = n - 1
        location_pointer = len(nums1)-1
        while j>=0 and k>=0:
            if nums1[j] > nums2[k]:
                nums1[location_pointer] = nums1[j]
                j -=1
            else:
                nums1[location_pointer] = nums2[k]
                k-=1
            location_pointer -=1
        if k < 0 and j>=0 and location_pointer != j:
            while j>=0:
                nums1[location_pointer] = nums1[j]
                j-=1
                location_pointer -=1
        if j<0 and k>=0:
            while k>=0:
                nums1[location_pointer] = nums2[k]
                k -= 1
                location_pointer -= 1
        return

obj = Solution()
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
obj.merge(nums1, m , nums2, n)
print nums1
