class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        counter = 0
        
        print(bin(x)[2:].zfill(8))
        print(bin(y)[2:].zfill(8))
        
        max_length = max(len(bin(x)), len(bin(y)))
        print('printing max ', max_length)
        
        print(bin(x)[2:].zfill(max_length))
        print(bin(y)[2:].zfill(max_length))
        
        for x, y in zip(bin(x)[2:].zfill(max_length), bin(y)[2:].zfill(max_length)):
            if x != y:
                counter +=1
                
        print(counter)
        
        return counter
