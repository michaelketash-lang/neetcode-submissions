class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)# creating a hash map: {letter:freq}
        maxHeap = [[-c,letter] for letter,c in count.items()]
        heapq.heapify(maxHeap) # creating min heap with -count cause dont have maxheap in python
        
        res = ""
        prev = None
        #greedy approach to get rid of the most freq letter
        while prev or maxHeap:
            if prev and not maxHeap: #we cant find a solution
                return ""
            cnt,char = heapq.heappop(maxHeap) #popping from heap
            
            res += char #concatenate the char(most freq)
            cnt += 1 
            if prev: #if prev exist we can add him back to heap
                heapq.heappush(maxHeap,prev)
                prev = None
            if cnt != 0:
                prev = [cnt,char]
        return res
