import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []
        incomingEdgeList = collections.defaultdict(int)
        adjList = collections.defaultdict(list)
        for i in range(numCourses):
            adjList[i] = []
        for curPreReq in prerequisites:
            incomingEdgeList[curPreReq[0]]+= 1
            adjList[curPreReq[1]].append(curPreReq[0])
        result = []
        stack = []
        for i in range(numCourses):
            if i not in incomingEdgeList:
                stack.append(i)
        while len(stack) > 0:
            selectedCourse = stack.pop()
            result.append(selectedCourse)
            if selectedCourse in adjList:
                curOutGoingEdges = adjList[selectedCourse]

                for outEdge in curOutGoingEdges:
                    incomingEdgeList[outEdge] -=1
                    if incomingEdgeList[outEdge] == 0:
                        stack.append(outEdge)
        return result if len(result) == numCourses else []

        # while len(incomingEdgeList) != 0:



obj = Solution()
numCourses = 4
preReq = [[1,0],[2,0],[3,1],[3,2]]
print obj.findOrder(numCourses, preReq)
numCourses = 2
preReq = [[1,0],[0,1]]
print obj.findOrder(numCourses, preReq)
numCourses = 10
preReq = []
print obj.findOrder(numCourses, preReq)


