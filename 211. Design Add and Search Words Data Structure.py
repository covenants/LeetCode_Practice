class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        
        node['$'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if ch not in node:
                    if ch == '.':
                        for x in node:
                            if x!= '$' and search_in_node(word[i+1:], node[x]):
                                return True
                    return False
                
                else:
                    node = node[ch]
            
            return '$' in node
        
        
        return search_in_node(word, self.trie)
    
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Using defaultdict and set

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.d[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        m = len(word)
        
        for dict_word in self.d[m]:
            
            i = 0
            
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i +=1
            if i == m:
                return True
            
        return False
