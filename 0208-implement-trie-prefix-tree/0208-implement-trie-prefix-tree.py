'''
Timestamps:
    Cases: 1:56
    Design: 7:56
    Verify: 11:57
    Code: 16:48
    
Understand and cases:
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["boy"], ["boil"], ["boy"], ["bo"], ["boil"], ["boil"]]

Design and verify:
    class TrieNode:
        def __init___(self, children: dict = {}, ends_word: bool = False):
            self.ends_word = bool
            self.children = children
            
    root
    b(f)
    o(f)
    y(t)i(f)
        l(t)
            
    init:
        self.root = TrieNode()
        
    insert:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
                continue
            
            new_node = TrieNode()
            node.children[c] = new_node
            node = new_node
        
        node.ends_word = True
        
    search:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            
            node = node.children[c]
            
        return node.ends_word
        
    startsWith:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            
            node = node.children[c]
        
        return True
'''
class TrieNode:
    def __init__(self):
        self.ends_word = False
        self.children = {}
            
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # start at our dummy root
        node = self.root
        
        # for each character in the word
        for c in word:
            # if it's already in the trie just move to it and continue
            if c in node.children:
                node = node.children[c]
                continue
            
            # otherwise add a new trie node, add the new node to the current node's
            # children, and then move to the new node
            new_node = TrieNode()
            node.children[c] = new_node
            node = new_node
        
        # after we've progressed to the last character and exited our loop
        # ensure to signify that the last character ends a word
        node.ends_word = True

    def search(self, word: str) -> bool:
        # start at our dummy root
        node = self.root

        # for each character in the word
        for c in word:
            # if it is not in our current nodes children
            # it does not exist
            if c not in node.children:
                return False
            
            # otherwise move to our next node
            node = node.children[c]
        
        # at the end return if the last character is the end of a word
        # or was simply added from a longer word with the current word
        # as a prefix
        return node.ends_word

    def startsWith(self, prefix: str) -> bool:
        # start at our dummy root
        node = self.root
        
        # for each character in the word
        for c in prefix:
            # if it is not in our current nodes children
            # it does not exist
            if c not in node.children:
                return False
            
            # otherwise move to our next node
            node = node.children[c]
        
        # if the entire prefix exists in the Trie return true
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)