# Design a data structure that follows the constraints of a Least 
# Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Constraints:
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.

# Example:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

# To implement an LRU (Least Recently Used) Cache with O(1) time complexity
#  for both get and put operations, we use:
# A hashmap to store key-value pairs for fast access.
# A doubly linked list to track the usage order of keys
# (most recently used at the front, least recently used at the back).

# Step-by-Step Explanation
# 1. Initialization:
#     self.cache: Hashmap for O(1) access to nodes by key.
#     self.head and self.tail: Dummy nodes to simplify insert/remove logic.
#     Doubly linked list maintains usage order:
#         Most recently used node is next to tail.
#         Least recently used node is next to head.
# 2. get(key):
#     If key exists:
#         Move node to tail (MRU position).
#         Return its value.
#     Else, return -1.
# 3. put(key, value):
#     If key exists:
#         Update value and move node to tail.
#     Else:
#         If cache is full:
#             Remove LRU node (head.next).
#             Delete from hashmap.
#         Insert new node and move to tail.
# 4. Helper Methods:
#     _remove(node): Detaches a node from the list.
#     _add_to_tail(node): Inserts a node before the tail.

# get	O(1)	Hashmap lookup + constant-time list operations
# put	O(1)	Hashmap insert/update + constant-time list operations
# Space	O(capacity)	Stores up to capacity nodes and hashmap entries


# Node class for doubly linked list
class Node:
    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# LRU Cache class
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Hashmap: key -> Node

        # Dummy head and tail nodes to simplify edge operations
        self.head = Node()
        self.tail = Node()

        # Link head and tail together
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_tail(self, node: Node):
        """Insert a node right before the tail (most recently used position)."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        """Return the value of the key if present, else -1. Move accessed node to tail."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)         # Remove from current position
            self._add_to_tail(node)    # Move to most recently used position
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """Insert or update the key-value pair. Evict LRU if capacity exceeded."""
        if key in self.cache:
            # Update existing node and move to tail
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            # Evict least recently used node if at capacity
            if len(self.cache) >= self.cap:
                lru = self.head.next       # Least recently used node
                self._remove(lru)
                del self.cache[lru.key]

            # Add new node to cache and move to tail
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)