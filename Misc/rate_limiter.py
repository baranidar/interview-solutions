class RateLimiter:
    def __init__(self):
     self.d = defaultdict(deque)
     self.rate_limit = 100
     self.time_limit = 1

    def is_valid(self, client_id):
        print(f"Length : {len(self.d[client_id])}")
        if len(self.d[client_id]) < self.rate_limit:
            return True
        elif time.time() - self.d[client_id][0] < self.time_limit:
            return False
        return True

    def add_request(self, client_id):
        if len(self.d[client_id]) == self.rate_limit:
            self.d[client_id].popleft()
        self.d[client_id].append(time.time())
        print(f"After adding : {self.d[client_id]}")

    def process(self, client_id):
        valid = self.is_valid(client_id)
        self.add_request(client_id)
        return valid