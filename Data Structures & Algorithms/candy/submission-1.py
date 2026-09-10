class Solution:
    def candy(self, ratings: List[int]) -> int:
        #initialize lst that each child gets 1 candy
        lst = [1]*len(ratings)
        #scan from indx 1 and check if i am bigger then left 
            # add the prev amount +1
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                lst[i] = lst[i-1] + 1
        # scan from the prev to end and check if i am bigger then my right:
            #take the max of my curr amount and the right + 1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                lst[i] = max(lst[i],lst[i+1]+1)
        # sum the candies
        return sum(lst)