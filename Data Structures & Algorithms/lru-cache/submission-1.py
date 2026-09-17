class Node:
    def __init__(self, key, val):
        self.key,self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapi = {} # we will map key to node

        self.left = Node(0,0) #least recent used
        self.right = Node(0,0) # most recent used

        self.left.next,self.right.prev = self.right,self.left
    
    def removeNode(self, node):
        prev , nxt = node.prev, node.next
        prev.next , nxt.prev = nxt , prev
    
    def insertNode(self , node): #insert to the right most 
        prev , nxt = self.right.prev , self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.mapi:
            #update the node to be most recent used
            #how can we do it?
            #we can delete the current node
            # we can insert the new node to the right most which is most recent used
            node = self.mapi[key]
            self.removeNode(node)
            self.insertNode(node)
            return self.mapi[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mapi:
            self.removeNode(self.mapi[key])
        self.mapi[key] = Node(key,value)
        self.insertNode(self.mapi[key])

        if len(self.mapi) > self.cap:
            lru = self.left.next
            self.removeNode(lru)
            del self.mapi[lru.key]
        
