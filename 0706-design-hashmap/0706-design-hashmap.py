'''
Timestamps:
    Cases: 1:00
    Design: 12:09
    Verify: 13:09
    Code:

Cases:
    ["MyHashMap", "put", "put", "get", "get", "remove", "get"]
    [[], [1, 2], [1, 2], [1], [3], [1], [1]]
    
Design and Verify:
    ListNodes to hold key & value
    % 987 as our hash
    class ListNode:
        def __init__(self, key, value, next = None):
            self.key = key
            self.value = value
            self.next = next
    
    hmap = [None for _ in range(hash)]
    hash = 987
    
    bucket = key % self.hash
    node = hmap[bucket]
    while node:
        if node.key = key:
            node.value = value
        
        if node.next:
            node = node.next
            
    if node:
        node.next = new ListNode(key, value)
    else:
        hmap[bucket] = node
        
        
        
    bucket = key % self.hash
    node = hmap[bucket]
    while node:
        if node.key = key:
            return value
            
    return -1
    
    
    
    bucket = key % self.hash
    node = hmap[bucket]
    last_node = node
    while node:
        if node.key = key:
            last_node.next = node.next
        
        last_node = node
        node = node.next
'''
class ListNode:
    def __init__(self, key, value, next_node = None):
        self.key = key
        self.value = value
        self.next = next_node

class MyHashMap:

    def __init__(self):
        self.hash = 987
        self.hmap = [None for _ in range(self.hash + 1)]

    def put(self, key: int, value: int) -> None:
        bucket = key % self.hash
        node = self.hmap[bucket]
        last_node = node
        while node:
            if node.key == key:
                node.value = value
                return

            last_node = node
            node = node.next

        if last_node:
            last_node.next = ListNode(key, value)
        else:
            self.hmap[bucket] = ListNode(key, value)

    def get(self, key: int) -> int:
        bucket = key % self.hash
        node = self.hmap[bucket]
        while node:
            if node.key == key:
                return node.value
            
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        bucket = key % self.hash
        node = self.hmap[bucket]
        
        if node and node.key == key:
            self.hmap[bucket] = node.next
            print(self.hmap[bucket])
        
        last_node = node
        while node:
            if node.key == key:
                last_node.next = node.next
                return

            last_node = node
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)