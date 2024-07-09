class Trie:
    def __init__(self) -> None:
        self.root = {}
        self.is_word = False
        
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.is_word] = True
        
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.is_word in node
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
   
 
trie = Trie()
print(trie.search("apple"))   # returns false
print(trie.insert("apple"))
print(trie.search("app"))     # returns false
print(trie.startsWith("app")) # returns true
print(trie.insert("app"))
print(trie.search("app"))     # returns true