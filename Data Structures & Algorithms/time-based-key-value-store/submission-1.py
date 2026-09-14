class TimeMap:

    def __init__(self):
        self.mapi = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapi[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res , values_list = "" , self.mapi[key]
        l , r = 0 , len(values_list) -1

        while l <= r:
            mid = (r + l) // 2
            if values_list[mid][1] > timestamp:
                r = mid - 1
            else:
                res = values_list[mid][0]
                l = mid + 1
        return res
