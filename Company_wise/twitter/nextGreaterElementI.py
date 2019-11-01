import collections
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0:
            return []
        stack = []
        hashmap = collections.defaultdict(int)
        for i in range(len(nums2)):
            while len(stack) !=0 and nums2[i] >= stack[-1]:
                element = stack.pop()
                hashmap[element] = nums2[i]
            stack.append(nums2[i])
        while len(stack)!=0:
            element = stack.pop()
            hashmap[element] = -1
        result = []
        for target in nums1:
            result.append(hashmap[target])
        return result

    def nextGreaterElement1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0:
            return []
        num2_dict = collections.defaultdict(int)
        for i in range(len(nums2)):
            num2_dict[nums2[i]] = i
        result = []
        for target in nums1:
            start_index = num2_dict[target]
            found = -1
            for j in range(start_index +1, len(nums2)):
                if nums2[j] > target:
                    found = nums2[j]
                    break
            result.append(found)
        return  result
obj = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print obj.nextGreaterElement(nums1, nums2), "E: [-1,3,-1]"
nums1 = [2,4]
nums2 = [1,2,3,4]
print obj.nextGreaterElement(nums1, nums2), "E:[3,-1]"