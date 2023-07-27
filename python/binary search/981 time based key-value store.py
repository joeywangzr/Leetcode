class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.time_map:
            return res
        values = self.time_map[key]
        l = 0
        r = len(values)-1
        
        while l <= r:
            mid = (l+r)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid+1 # must be lower or equal to target
            else:
                r = mid-1
        return res
    
obj = TimeMap()
obj.set("foo","bar",1)
print(obj.get("foo",1)) # bar
print(obj.get("foo",3)) # bar
obj.set("foo","bar2",4)
print(obj.get("foo",4)) # bar2
print(obj.get("foo",5)) # bar2