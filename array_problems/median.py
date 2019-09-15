# from __future__ import division
__author__ = 'mushahidalam'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        if n == 0 or m == 0:
            if n == 0:
                if m % 2 == 0:
                    median = ((m) / 2) + 1
                    return (nums2[median - 1] + nums2[median - 2]) / 2.0
                else:
                    median = m / 2
                    return nums2[median]
            if m == 0:
                if n % 2 == 0:
                    median = ((n) / 2) + 1
                    return (nums1[median - 1] + nums1[median - 2]) / 2.0
                else:
                    median = n / 2
                    return nums1[median]

        if ((n + m) % 2) == 0:
            # print("asdasd")
            median = ((n + m) / 2) + 1
            i = 0
            j = 0
            k = 0
            result = []
            count = 0
            while i != n and j != m:
                if nums1[i] > nums2[j]:
                    result.append(nums2[j])
                    k += 1
                    j += 1
                    count += 1
                    if count == median:
                        med = (result[k - 1] + result[k - 2]) / 2.0
                        return med
                else:
                    result.append(nums1[i])
                    k += 1
                    i += 1
                    count += 1
                    if count == median:
                        med = (result[k - 1] + result[k - 2]) / 2.0
                        return med
            while i != n:
                result.append(nums1[i])
                k += 1
                i += 1
                count += 1
                if count == median:
                    med = (result[k - 1] + result[k - 2]) / 2.0
                    return med

            while j != m:
                result.append(nums2[j])
                k += 1
                j += 1
                count += 1
                if count == median:
                    med = (result[k - 1] + result[k - 2]) / 2.0
                    return med
        else:
            median = ((n + m) / 2) + 1
            i = 0
            j = 0
            k = 0
            result = []
            count = 0
            while i != n and j != m:
                if nums1[i] > nums2[j]:
                    result.append(nums2[j])
                    k += 1
                    j += 1
                    count += 1
                    if count == median:
                        med = result[k - 1]
                        return med
                else:
                    result.append(nums1[i])
                    k += 1
                    i += 1
                    count += 1
                    if count == median:
                        med = result[k - 1]
                        return med
            while i != n:
                result.append(nums1[i])
                k += 1
                i += 1
                count += 1
                if count == median:
                    med = result[k - 1]
                    return med

            while j != m:
                result.append(nums2[j])
                k += 1
                j += 1
                count += 1
                if count == median:
                    med = result[k - 1]
                    return med


A = [1, 2]
B = [1, 2, 3]
obj = Solution()
print obj.findMedianSortedArrays(A, B)
