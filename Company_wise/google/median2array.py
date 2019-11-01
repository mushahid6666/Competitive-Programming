'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
import sys
class Solution(object):
    def merge2array(self, arr1, arr2):
        result = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i+=1
            else:
                result.append(arr2[j])
                j+=1
        while i < len(arr1):
            result.append(arr1[i])
            i += 1
        while j < len(arr2):
            result.append(arr2[j])
            j += 1
        return result

    #Merging two array Solution
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_arr = self.merge2array(nums1, nums2)
        if len(merged_arr) %2 != 0:
            median = merged_arr[(len(merged_arr) / 2 )]
            return float(median)
        else:
            middle_index = (len(merged_arr) / 2 )- 1
            median = (float(merged_arr[middle_index]) + merged_arr[middle_index + 1] ) / 2
            return median

    #log(min(m+s)) solution
    def findMedianSortedArrays(self, nums1, nums2):
        x = len(nums1)
        y = len(nums2)
        if x > y :
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = x
        while (low <= high):
            partition_x = (low + high) / 2
            # sum of partition_x + partition_y should be = half of combined array
            #hence subtract by partition_x , +1 to make work for both even and odd case
            partition_y =( (x+ y + 1) /2 ) - partition_x

            #if no elements on left of array of x
            max_left_partition_x = -sys.maxint if partition_x==0 else nums1[partition_x -1 ]
            min_right_partition_x = sys.maxint if partition_x == x else nums1[partition_x]

            # if no elements on left of array of y
            max_left_partition_y = -sys.maxint if partition_y == 0 else nums2[partition_y - 1]
            min_right_partition_y = sys.maxint if partition_y == y else nums2[partition_y]

            # Median found
            if max_left_partition_x <= min_right_partition_y and max_left_partition_y <= min_right_partition_x:
                # if even
                if (x + y) % 2 == 0:
                    return (float(max(max_left_partition_x, max_left_partition_y) + min(min_right_partition_x,
                                                                                        min_right_partition_y)) / 2)
                else:
                    return float(max(max_left_partition_x, max_left_partition_y))
            elif max_left_partition_x > min_right_partition_y:
                high = partition_x - 1
            else:
                low = partition_x + 1



obj = Solution()
arr1 = [1,3]
arr2 = [2]
print obj.findMedianSortedArrays(arr1, arr2)
arr1 = [1,2]
arr2 = [3,4]
print obj.findMedianSortedArrays(arr1, arr2)
arr1 = [2]
arr2 = []
print obj.findMedianSortedArrays(arr1, arr2)