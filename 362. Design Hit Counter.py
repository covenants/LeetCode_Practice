class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hitcounter = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hitcounter.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        x = 0
        
        for i in range(len(self.hitcounter)-1, -1, -1):
            if timestamp - self.hitcounter[i] < 300:
                x +=1
            else:
                break
        
        print(x)
        
        return x
        
