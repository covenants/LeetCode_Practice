class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        number_of_strings = len(strs)
        
        i, j = 0, 0
        flag = 0
        matched_char = []
        
        min_len = min([len(x) for x in strs])
        
        while i < min_len:
            flag = 0
            j =0
            char = strs[0][i]
            print(i, char, matched_char)
            
            while j < number_of_strings:
                
                if char != strs[j][i]:
                    flag = 1
                    break
                    
                j +=1
                
            if flag == 0:
                matched_char.append(char)
            if flag == 1:
                break
            
            i+=1
        
        print(matched_char)
        
        return "".join(matched_char)
                    
            
        
