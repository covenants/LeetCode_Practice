from collections import defaultdict

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.o = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.o[key].append([timestamp, value])
        
        
        
    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.o:
            
            # total values
            ind = len(self.o[key]) -1
            
            # return the earliest time greater than queried time
            while ind > -1 and self.o[key][ind][0] > timestamp:
                ind -=1
                
            if ind == -1:
                return ""
            else:
                return self.o[key][ind][1]
                    
        else:
            return ""
