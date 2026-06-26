import datetime

class LruCache:
    def __init__(self, limit):
        if limit < 1:
            raise ValueError("Cache limit should be more than or equal to 1")
        self.cache = []
        self.limit = limit

    def set(self, key, value):
        while len(self.cache) >= self.limit:
            oldest = min(self.cache, key=lambda data: data["time"])
            self.cache.remove(oldest)
        self.cache.append({key: value, "time": datetime.datetime.now()})
    
    def get(self, key):
        for data in self.cache:
            if key in data:
                data["time"] = datetime.datetime.now()
                return data[key]