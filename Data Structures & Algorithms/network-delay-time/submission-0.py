class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for x,y,time in times:
            graph[x].append((y,time))
        
        dist = {node : float("inf") for node in range(1, n + 1)}
        q = deque([(k , 0)])

        dist[k] = 0

        while q:
            node , time = q.popleft()
            if dist[node] < time:
                continue
            
            for neighbor , t in graph[node]:
                if time + t < dist[neighbor]:
                    dist[neighbor] = time + t
                    q.append((neighbor, time + t))
        res = max(dist.values())
        return res if res < float("inf") else -1