// Official solution

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)
        
        #print(wordSet)
        
        memo = defaultdict(list)
        
        
        def _wordBreak_topdown(s):
            
            if not s:
                return [[]]
            
            if s in memo:
                return memo[s]
            
            for endIndex in range(1, len(s) + 1):
                
                # slowly increase the word from first character
                word = s[:endIndex]
                #print(word)
                
                # is the word in the wordSet
                if word in wordSet:
                    # check if rest of the strings are as word in the wordSets
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]
                    
        
        _wordBreak_topdown(s)
        
        print([" ".join(words) for words in memo[s]])
        
        return [" ".join(words) for words in memo[s]]
        
