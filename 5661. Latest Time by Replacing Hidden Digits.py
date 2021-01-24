class Solution:
    def maximumTime(self, time: str) -> str:
        
        max_value = ['2', '3', ':', '5', '9']
        
        first_char = ['0','1','2']
        seconrd_char = []
        
        time = list(time)
        
        t = time.copy()
        
        
        #print(' time ', time)
        
        if t[0] != '?' and t[1] == '?':
            if t[0] == '0':
                t[1] = '9'
            if t[0] == '1':
                t[1] = '9'
            if t[0] == '2':
                t[1] = '3'
                
        elif t[0] == '?' and t[1] != '?':
            if t[1] in ['1', '2', '3']:
                t[0] = '2'
                
            elif t[1] == '0':
                t[0] = '2'
            else:
                t[0] = '1'
                
        elif t[0] == '?' and t[1] == '?':
            t[0] = '2'
            t[1] = '3'
        
        
        if t[3] == '?':
            t[3] = '5'
        
        if t[4] == '?':
            if t[3] in ['0', '1', '2', '3', '4', '5']:
                t[4] = '9'
            else:
                t[4] = '0'  
            
        print(t)
            
        x = ''.join(t)
        
        return x
