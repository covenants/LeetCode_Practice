class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        output = defaultdict(list)
        
        def string_to_tuple(word):
            
            if len(word) > 1:
                
                lst = []
                
                for s in range(len(word)-1):
                    
                    diff = ord(word[s]) - ord(word[s+1])
                    
                    if diff < 0:
                        diff = diff + 26
                    
                    
                    lst.append(diff)
                
                print('word ', word, ' lst ', lst)
                return tuple(lst)
            
            else:
                return 1
            
        
        for word in strings:
            output[string_to_tuple(word)].append(word)
        
        result = []
        
        ##############
        for key, values in output.items():
            print(key, values)
            result.append(values)
        
        print(result)
        ### can be written as following
        ###############
        
        return [output[s] for s in output]
