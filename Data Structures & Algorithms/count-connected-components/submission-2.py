class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        graph = defaultdict(list)
        visit = set()

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(i):
            stack =[i]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        stack.append(neighbor)


        for i in range(n):
            if i not in visit:
                components += 1
                visit.add(i)
                dfs(i)
        
        return components