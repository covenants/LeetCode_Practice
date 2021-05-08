class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # placeholder to store total time
        d = [0] * n
        
        add_time = 0
        
        stack = []
        
        for item in logs:
            id, status, time = str(item).split(":")    
            id = int(id)
            time = int(time)
            #print(id, status, time)
            
            if status == 'start':
                stack.append([id, status, time])
            
            # status ends and id matches
            elif status == 'end' and id == stack[-1][0]:
                old_id, old_status, old_time = stack.pop()
                add_time = time - old_time + 1
                d[id] += add_time
                
                # for removing overlapped time
                # remove the intermediate process time
                if stack:
                    d[stack[-1][0]] = d[stack[-1][0]] - add_time
                    
            
        return d
    
    
                
                
                
