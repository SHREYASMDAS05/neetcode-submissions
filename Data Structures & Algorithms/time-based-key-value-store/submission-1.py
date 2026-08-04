class TimeMap:

    def __init__(self):
        self.timemap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value , timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        l = 0
        r = len(self.timemap[key]) - 1
        #or can use len(timestamp[key])
        #convert it to array 
        arr = self.timemap[key]
        res = ''
        while l <=r:
            m = (l + r) // 2
                

            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1


        return res


        
