import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        frequencyMap = collections.defaultdict(int)
        for i in range(len(nums)):
            frequencyMap[nums[i]] += 1

        bucket = [[]for _ in range(len(nums) + 1)]
        for key in frequencyMap.keys():
            curFreq = frequencyMap[key]
            bucket[curFreq].append(key)

        result = []
        j = len(bucket) -1
        m = 0
        while j >=0  and m < k:
            if len(bucket[j]) != 0:
                cur_list = bucket[j]
                while m < k and len(cur_list) > 0:
                    result.append(cur_list.pop())
                    m+=1
            j-=1
        return result

solObj = Solution()
nums = [1,1,1,2,2,3]
k = 2
print solObj.topKFrequent(nums, k)
nums = [1]
k = 1
print solObj.topKFrequent(nums, k)
