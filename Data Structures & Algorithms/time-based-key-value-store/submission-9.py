class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dic.get(key, None) is not None:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]
        print(self.dic.items())
        return 

    def get(self, key: str, timestamp: int) -> str:
        cur = self.dic.get(key)
        if not cur:
            return ""
        
        # Binary search for rightmost timestamp ≤ target
        left, right = 0, len(cur) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if cur[mid][0] <= timestamp:
                result = mid  # valid candidate
                left = mid + 1  # look for better one to the right
            else:
                right = mid - 1
        
        return cur[result][1] if result != -1 else ""
        
