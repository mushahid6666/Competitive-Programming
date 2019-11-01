import collections
class Solution(object):
    def checkNodeExistsWithOutgoingEdge(self, indegree_list, inc_edjes_dict):
        inc_edge_zero_nodes = []
        for i in range(len(indegree_list)):
            if indegree_list[i] == 0:
                inc_edge_zero_nodes.append(i)

        for node in inc_edge_zero_nodes:
            if node in inc_edjes_dict:
                return node
        return None
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0 or numCourses == 0:
            return True
        inc_edjes_dict = collections.defaultdict(list)
        indegree_list = [0] * numCourses
        for edje in prerequisites:
            inc_edjes_dict[edje[1]].append(edje[0])
            indegree_list[edje[0]] += 1
        node = self.checkNodeExistsWithOutgoingEdge(indegree_list, inc_edjes_dict)
        while node != None:
            out_edge = inc_edjes_dict[node]
            for target_node in out_edge:
                indegree_list[target_node] -= 1
            del inc_edjes_dict[node]
            node = self.checkNodeExistsWithOutgoingEdge(indegree_list, inc_edjes_dict)

        if indegree_list.count(0) != numCourses:
            return False
        return True





obj = Solution()
numCourses = 3
prerequisites = [[1,0],[2,1],[0,2]]
print obj.canFinish(numCourses, prerequisites)
numCourses = 2
prerequisites = [[1,0]]
print obj.canFinish(numCourses, prerequisites)
numCourses = 2
prerequisites = [[1,0],[0,1]]
print obj.canFinish(numCourses, prerequisites)

