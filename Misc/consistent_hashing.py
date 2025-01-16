import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, nodes=None, replicas=3):
        self.nodes = nodes if nodes else []
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.replicas):
            key = self._hash(f"{node}:{i}")
            self.ring[key] = node
            self.sorted_keys.append(key)
        self.sorted_keys.sort()

    def remove_node(self, node):
        for i in range(self.replicas):
            key = self._hash(f"{node}:{i}")
            del self.ring[key]
            self.sorted_keys.remove(key)

    def get_node(self, key):
        if not self.ring:
            return None

        hash_value = self._hash(key)
        index = bisect.bisect_left(self.sorted_keys, hash_value)

        if index == len(self.sorted_keys):
            index = 0

        return self.ring[self.sorted_keys[index]]

if __name__ == "__main__":
    nodes = ["node1", "node2", "node3"]
    hash_ring = ConsistentHashRing(nodes)

    print(hash_ring.get_node("key1"))  # Output: node2
    print(hash_ring.get_node("key2"))  # Output: node3
    print(hash_ring.get_node("key3"))  # Output: node1

    hash_ring.add_node("node4")
    print(hash_ring.get_node("key1"))  # Output: node2 (likely, depending on hash values)