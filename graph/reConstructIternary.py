"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
 reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical
order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
["JFK",:"SFO","ATL"]
["SFO":"ATL"]
["ATL":"JFK","SFO"]



Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""
import collections, copy
class Solution(object):
    def __init__(self):
        self.itinerary = list()
        self.solutionfound = False

    def dfs_traverse(self, edje_map, outdegree_map, cur_node, curpath, visited_count):
        if self.solutionfound:
            return
        if outdegree_map[cur_node] == 0 and len(visited_count) == self.ticket_count:
            self.itinerary.append(curpath)
            self.solutionfound = True
            return
        visited_count.append(cur_node)
        for outgoingNode in edje_map[cur_node]:
            if self.solutionfound:
                return
            if outdegree_map[outgoingNode] == 0 and len(visited_count) -1 != self.ticket_count -1 :
                continue
            new_edge_map = copy.deepcopy(edje_map)
            new_edge_map[cur_node].remove(outgoingNode)
            new_outdegreemap = copy.deepcopy(outdegree_map)
            new_outdegreemap[cur_node] -=1
            newpath = list(curpath)
            newpath.append(outgoingNode)
            self.dfs_traverse(new_edge_map, new_outdegreemap, outgoingNode, newpath, list(visited_count))



    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if len(tickets) == 0:
            return []
        tickets = sorted(tickets)
        self.ticket_count = len(tickets)
        edje_map = collections.defaultdict(list)
        outdegree_map = collections.defaultdict(int)
        for cur_ticket in tickets:
            edje_map[cur_ticket[0]].append(cur_ticket[1])
            outdegree_map[cur_ticket[0]] +=1
        curpath = []
        curpath.append("JFK")
        self.dfs_traverse(copy.deepcopy(edje_map), copy.deepcopy(outdegree_map), "JFK", curpath, [])
        result_iter  = "".join(self.itinerary[0])
        result_iter_index = 0

        for i in range(1, len(self.itinerary)):
            new_iter = "".join(self.itinerary[i])
            if new_iter < result_iter:
                result_iter = new_iter
                result_iter_index = i

        return self.itinerary[result_iter_index]



obj = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["JFK", "LHR"]]
# tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
print obj.findItinerary(tickets)