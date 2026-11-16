class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course,demand in prerequisites:
            graph[course].append(demand)
        
        cycle , visited = set() , set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)
            for demand in graph[course]:
                if dfs(demand) == False:
                    return False
            
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return res