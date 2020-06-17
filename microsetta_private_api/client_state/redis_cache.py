import json
import redis


class RedisCache:
    # System Banner Format: ["Blah blah blah", "primary"]
    SYSTEM_BANNER = "system_banner"

    def __init__(self):
        self.r = redis.Redis(host='localhost',
                             port=6379,
                             db=0,
                             decode_responses=True)

    def __getitem__(self, key):
        val = self.r.get(key)
        if val is None:
            return None
        return json.loads(val)

    def get(self, key, default):
        val = self.r.get(key)
        if val is None:
            return default
        return json.loads(val)

    def __setitem__(self, key, value):
        self.r.set(key, json.dumps(value))

    def __delitem__(self, key):
        self.r.delete(key)
