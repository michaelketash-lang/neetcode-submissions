class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visit = set()
        for course , preq in prerequisites:
            graph[course].append(preq)
        
        
        def dfs(crs):
            if crs in visit:
                return False
            if graph[crs] == []:
                return True

            visit.add(crs)
            for neighbor in graph[crs]:
                if not dfs(neighbor):
                    return False
            visit.remove(crs)
            graph[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            