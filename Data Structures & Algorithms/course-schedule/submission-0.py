class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the graph 
        # we are gonna use a hash map that will map numCourse : prerequisites
        graph = collections.defaultdict(list)
        visit = set()

        for crs, prereq in prerequisites:
            graph[crs].append(prereq)
        
        # dfs we want to check if there is a cycle in the graph
        def dfs(i):
            if i in visit:
                return False
            
            if graph[i] == []:
                return True
            
            visit.add(i)
            for pre in graph[i]:
                if not dfs(pre):
                    return False
            
            visit.remove(i)
            graph[i] =[]
            return True


        # run dfs on every node in the graph that we didnt visit it
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True





