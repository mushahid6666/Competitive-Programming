class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0
        m = len(nums1)
        j = 0
        n = len(nums2)
        result = []
        count = 0
        stack = []
        while i < m and j < n and count < k:
            result.append([nums1[i], nums2[j]])
            count +=1
            if i+1 < m and j+1 < n:
                if nums1[i+1] < nums2[j+1]:
                    i+=1
                    stack.append([nums1[i], nums2[j+1:]])
                else:
                    j+=1
                    stack.append([nums1[i+1:], nums2[j]])
            elif i+1 < m:
                i+=1
            else:
                j+=1
        return result

obj = Solution()
# nums1 = [1,7,11]
# nums2 = [2,4,6]
# k = 3
# print obj.kSmallestPairs(nums1, nums2, k), "EXPECTED:[[1,2],[1,4],[1,6]] "
# nums1 = [1,1,2]
# nums2 = [1,2,3]
# k = 2
# print obj.kSmallestPairs(nums1, nums2, k),"EXPECTED:[1,1],[1,1]"
# nums1 = [1,2]
# nums2 = [3]
# k = 3
# print obj.kSmallestPairs(nums1, nums2, k),"EXPECTED:[1,3],[2,3]"
# nums1 = [1,2,4]
# nums2 = [3,10,20]
# k = 3
# print obj.kSmallestPairs(nums1, nums2, k),"EXPECTED:[1,3],[2,3],[4,3]"
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 6
print obj.kSmallestPairs(nums1, nums2, k)