# Given a set of candidate numbers (candidates) (without duplicates) and
# a target number (target), find all unique combinations in candidates where
# the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
import copy
class Solution(object):
    def getAllCombinationsTarget(self, candidates, target, resultArray, result, cursum, newCandidateIndex):
        curResultArray = copy.copy(resultArray)
        if newCandidateIndex != None:
            curResultArray.append(candidates[newCandidateIndex])
        curIterSum = copy.copy(cursum)
        if newCandidateIndex == None:
            newCandidateIndex = 0
        for i in range(newCandidateIndex, len(candidates)):
            candidate = candidates[i]
            if curIterSum > target:
                return
            if candidate <= target:
                if curIterSum + candidate == target:
                    curResultArray.append(candidate)
                    result.append(curResultArray)
                    return
                elif curIterSum + candidate < target:
                    self.getAllCombinationsTarget(candidates, target , curResultArray, result, curIterSum + candidate, i)
        return -1

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.getAllCombinationsTarget(candidates, target, [], result, 0 , None)
        return result

solObj = Solution()
candidates = [2,3,5]
target = 8
candidates = [2,3,6,7]
target = 7
print solObj.combinationSum(candidates, target)
