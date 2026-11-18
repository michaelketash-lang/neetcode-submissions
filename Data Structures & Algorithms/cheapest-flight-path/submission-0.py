from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n        
        # Build graph
        graph = defaultdict(list)
        for source, dest, price in flights:
            graph[source].append((dest, price))
            
        def bfs():
            # price , source node , number of stops
            queue = deque([(0, src, 0)])

            while queue:
                price, node, stops = queue.popleft()

                if stops > k:
                    continue

                for neighbor, cost in graph[node]:
                    update_cost = cost + price
                    if update_cost < prices[neighbor]:
                        prices[neighbor] = update_cost
                        queue.append((update_cost, neighbor, stops + 1))
            
            return prices[dst] if prices[dst] != float("inf") else -1
        
        return bfs()