class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []

        for passengers , start , end in trips:
            points.append([start , passengers])
            points.append([end , -passengers])
        
        cur_pass = 0
        points = sorted(points)
        for point , passengers in points:
            cur_pass += passengers
            if cur_pass > capacity:
                return False
        
        return True
            