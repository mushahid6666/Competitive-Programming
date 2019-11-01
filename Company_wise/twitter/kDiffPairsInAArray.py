import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numberDict = collections.defaultdict(int)
        for i in range(len(nums)):
            numberDict[nums[i]] +=1

        numPairs = set()
        if k <0:
            return 0
        if k==0:
            pairCount = 0
            for key in numberDict.keys():
                if numberDict[key] > 1:
                    pairCount +=1
            return pairCount
        for i in range(len(nums)):
            num1 = nums[i]
            target1 = num1 - k
            target2 = num1 + k
            if target1 in numberDict:
                pair = tuple([num1, target1]) if num1 < target1 else tuple([target1, num1])
                numPairs.add(pair)
            if target2 in numberDict:
                pair = tuple([num1, target2]) if num1 < target2 else tuple([target2, num1])
                numPairs.add(pair)
        # print numPairs
        return len(numPairs)

obj = Solution()
arr = [3, 1, 4, 1, 5]
k = 2
print obj.findPairs(arr, k)
arr = [1, 2, 3, 4, 5]
k = 1
print obj.findPairs(arr, k)
arr = [1, 3, 1, 5, 4]
k = 0
print obj.findPairs(arr, k)

