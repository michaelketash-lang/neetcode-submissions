class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build a graph -> with a hash map
        graph = collections.defaultdict(list)
        visit = set()
        components = 0 

        for x , y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        # we are gonna need a dfs algorithm we can use a bfs
        def dfs(i):
            for neighbor in graph[i]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    dfs(neighbor)

        #scan every node in the graph between 0 to n
        for i in range(n):
            if i not in visit:
                components += 1
                visit.add(i)
                dfs(i)
        
        return components
        # add the current node to visited
        # run the dfs
        #increment the #components by 1
        