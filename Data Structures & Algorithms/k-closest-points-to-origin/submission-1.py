class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        def kClosest(points):
            # creating max heap
            maxHeap = []
            # scan the points
            for point in points:
                # calculate the distance between origin and pooint
                x , y = point
                distance = (-1) * ((x ** 2) + (y ** 2))
                heapq.heappush(maxHeap , [distance , x , y])
                # check that size is not bigger than k
                if not (len(maxHeap) <= k):
                    heapq.heappop(maxHeap)
            return maxHeap

        maxHeap = kClosest(points)
        # we want to scan the heap and return the coordinate [x,y]
        while maxHeap:
            node = heapq.heappop(maxHeap)
            distance , x , y = node
            res.append([x,y])
        
        return res

