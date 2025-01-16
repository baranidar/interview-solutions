class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Hash map to store key-node pairs
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add_to_tail(self, node):
        """Add a node to the tail of the doubly linked list."""
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key):
        """Return the value of the key if present, else return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.value
        return -1

    def put(self, key, value):
        """Insert or update a key-value pair in the cache."""
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Example usage
lru_cache = LRUCache(2)  # Create an LRU cache with capacity 2
lru_cache.put(1, 1)      # Cache = {1=1}
lru_cache.put(2, 2)      # Cache = {1=1, 2=2}
print(lru_cache.get(1))  # Access 1, Cache = {2=2, 1=1}, Output: 1
lru_cache.put(3, 3)      # Add 3, Cache = {1=1, 3=3} (2 is removed as it's LRU)
print(lru_cache.get(2))  # 2 was removed, Output: -1
lru_cache.put(4, 4)      # Add 4, Cache = {3=3, 4=4} (1 is removed as it's LRU)
print(lru_cache.get(1))  # 1 was removed, Output: -1
print(lru_cache.get(3))  # Access 3, Cache = {4=4, 3=3}, Output: 3
print(lru_cache.get(4))  # Access 4, Cache = {3=3, 4=4}, Output: 4