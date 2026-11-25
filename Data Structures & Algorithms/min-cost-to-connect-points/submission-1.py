class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # we need to connect all points together
        # we want to build the graph
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            x1 , y1 = points[i]
            for j in range(i + 1 , n):
                x2 , y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([distance , j])
                graph[j].append([distance , i])
        
        res = 0
        minHeap = [[0,0]]
        visit = set()

        while len(visit) < n:
            cost , node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neighbor_cost , neighbor in graph[node]:
                if neighbor not in visit:
                    heapq.heappush(minHeap,[neighbor_cost , neighbor])
        
        return res


        
        # option : connect between every two nodes undirected edge
        # calculate the cost of the edge

        # run prim algo
