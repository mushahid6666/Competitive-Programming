class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #Correct approach
        #Get All possible pairs and sum
        #   then run through all possible pairs as 2 sum with no duplicates
        dict = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums [j]
                if sum in dict:
                    dict[sum].append((i, j))
                else:
                    dict[sum] = [(i, j)]
        result = set()
        for key in dict:
            twoSumTarget = target - key
            if twoSumTarget in dict:
                for (i,j) in dict[key]:
                    for (l,m) in dict[twoSumTarget]:
                        if i!=l and i!=m and j!=l and j!=m:
                            flist = [nums[i], nums[j], nums[l], nums[m]]
                            flist.sort()
                            result.add(tuple(flist))
        return result




obj = Solution()
# target = 0 # missing = [-2,-1,0,3]
# nums = [-3,-2,-1,0,0,1,2,3]
#[[-3, 3, -2, 2], [-3, 3, -1, 1], [-3, 3, 0, 0], [-3, 2, 0, 1],                      [-2, 2, -1, 1], [-2, 2, 0, 0], [-1, 1, 0, 0]]
#Expected
# [[-3,-2,2,3],  [-3,-1,1,3],      [-3,0,0,3],      [-3,0,1,2],       [-2,-1,0,3],  [-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# [[-3, 3, -2, 2], [-3, 3, -1, 1], [-3, 3, 0, 0],                  [-2, 3, -1, 0], [-2, 2, -1, 1], [-2, 2, 0, 0], [-1, 1, 0, 0]]

nums = [-3,-1,0,2,4,5]
target = 2 #Answer = [[-3,-1,2,4]]
print obj.fourSum(nums,target)