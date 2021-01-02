class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = collections.defaultdict(list)
        
        for s in strs:
            answer[''.join(sorted(list(s)))].append(s)
            
        result = []
        for k, v in answer.items():
            #print(v)
            result.append(v)
            
        return result
                
        
