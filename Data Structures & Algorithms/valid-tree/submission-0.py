class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge case
        if len(edges) > n - 1:
            return False
        # build the graph
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visit = set()

        def bfs():
            q = deque([(0 , -1)]) 
            visit.add(0)

            while q:
                node , parent = q.popleft()
                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    
                    if neighbor in visit:
                        return False
                    
                    visit.add(neighbor)
                    q.append((neighbor , node))
        bfs()
        return len(visit) == n