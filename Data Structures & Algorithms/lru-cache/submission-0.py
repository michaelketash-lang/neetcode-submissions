class Node:
    def __init__(self, key, val):
        self.key = key      # Store key to delete from hashmap later
        self.val = val      # Store the actual value
        self.prev = None    # Pointer to the previous node
        self.next = None    # Pointer to the next node

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity        # Max capacity of the cache
        self.cache = {}                 # Hashmap to store key -> Node
        
        # Initialize dummy nodes to avoid null checks
        self.left = Node(0, 0)          # Left dummy node (Least Recently Used side)
        self.right = Node(0, 0)         # Right dummy node (Most Recently Used side)
        
        # Connect the dummy nodes to each other
        self.left.next = self.right     # Left points to Right
        self.right.prev = self.left     # Right points to Left

    # Helper: remove a node from the linked list
    def remove(self, node):
        prev = node.prev                # Get the node before the target
        nxt = node.next                 # Get the node after the target
        prev.next = nxt                 # Skip target: connect prev directly to next
        nxt.prev = prev                 # Skip target: connect next directly to prev

    # Helper: insert a node at the right (MRU position)
    def insert(self, node):
        prev = self.right.prev          # The current last real node
        nxt = self.right                # The right dummy node
        
        prev.next = node                # Old last node points to new node
        nxt.prev = node                 # Right dummy points to new node
        
        node.next = nxt                 # New node points to right dummy
        node.prev = prev                # New node points to old last node

    def get(self, key: int) -> int:
        if key in self.cache:           # Check if key exists in hashmap
            self.remove(self.cache[key])    # Remove node from current position
            self.insert(self.cache[key])    # Move node to the right (MRU)
            return self.cache[key].val      # Return the value
        return -1                       # Return -1 if key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:           # If key already exists
            self.remove(self.cache[key])    # Remove the old node
        
        self.cache[key] = Node(key, value)  # Create new node and add to map
        self.insert(self.cache[key])        # Insert new node at right (MRU)
        
        if len(self.cache) > self.capacity: # Check if capacity is exceeded
            lru = self.left.next            # Identify the LRU node (next to left dummy)
            self.remove(lru)                # Remove LRU node from list
            del self.cache[lru.key]         # Remove LRU key from hashmap
