import copy, sys
class Solution(object):

    def __init__(self):
        self. cycle_edges = list()
        self.found_cycle = False
    def dfs(self, vertex, prev_vertex, vertices_map, visited_list):
        if self.found_cycle == True:
            return

        if vertex in visited_list:
            # print visited_list
            cycle_start_index = visited_list.index(vertex)
            cycle_list = visited_list[cycle_start_index:]

            cycle_list.append(vertex)
            # print cycle_list
            self.found_cycle = True
            for i in range(len(cycle_list)-1, 0 , -1):
                self.cycle_edges.append([cycle_list[i], cycle_list[i-1]])
            return
        visited_list.append(vertex)
        for neighbour in vertices_map[vertex]:

            if neighbour != prev_vertex:
                new_visited_list = copy.deepcopy(visited_list)
                self.dfs(neighbour, vertex, vertices_map, new_visited_list)

    def findCyle(self, vertices_map):
        """
        :param vertices_map: dict
        :return:
        """
        for vertex in vertices_map:
            self.dfs(vertex, None, vertices_map, [])


    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.__init__()
        vertices_map = dict()
        for edge in edges:
            if edge[0] in vertices_map:
                vertices_map[edge[0]].append(edge[1])
            else:
                vertices_map[edge[0]] = [edge[1]]
            if edge[1] in vertices_map:
                vertices_map[edge[1]].append(edge[0])
            else:
                vertices_map[edge[1]] = [edge[0]]
        # print vertices_map
        self.findCyle(vertices_map)
        # print self.cycle_edges
        max_index = -sys.maxint
        for edge in self.cycle_edges:
            if edge in edges:
                index = edges.index(edge)
                max_index = max(max_index, index)
            else:
                reverse_edge = [edge[1], edge[0]]
                if reverse_edge in edges:
                    index = edges.index(reverse_edge)
                    max_index = max(max_index, index)
        return edges[max_index]







obj = Solution()
# input = [[1,2], [1,3], [2,3]]
# #Output: [2,3]
# print obj.findRedundantConnection(input)
# input= [[1,2], [2,3], [3,4], [1,4], [1,5]]
# # Output: [1,4]
# print obj.findRedundantConnection(input)
input = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
print obj.findRedundantConnection(input)