import  collections
class Solution(object):
    def dfs_graph(self, node, color):
        if node in self.visited_nodes:
            return
        self.visited_nodes.add(node)
        self.color_nodes[node] = color
        for edje in self.edje_list[node]:
            self.dfs_graph(edje, color)


    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.edje_list = collections.defaultdict(list)
        for i in range(len(M)):
            self.edje_list[i]= list()
            for j in range(len(M[0])):
                if i==j:
                    continue
                if M[i][j] ==1:
                    self.edje_list[i].append(j)

        self.visited_nodes = set()
        self.color_nodes = collections.defaultdict(int)
        for i in range(len(M)):
            self.color_nodes[i] = i
        for i in range(len(M)):
            self.dfs_graph(i, self.color_nodes[i])
        subgraph = set(self.color_nodes.values())
        return len(subgraph)


obj = Solution()
matrix = [[1,1,0],
        [1,1,0],
        [0,0,1]]

print obj.findCircleNum(matrix)

matrix = [[1,1,0],
 [1,1,1],
 [0,1,1]]
print obj.findCircleNum(matrix)