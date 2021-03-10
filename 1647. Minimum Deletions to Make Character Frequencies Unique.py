class Solution:
    def minDeletions(self, s: str) -> int:
        
        frequency = collections.Counter(s)

        # total unique characters, we need to make sure they all have unique values
        total = len(frequency.keys())
        
        total_deletes = 0
        unique_values = []
        
        sorted_values = sorted(frequency.values(), reverse=True)
        
        for i in sorted_values:
            print('i in sorted values ', i)
            if i not in unique_values:
                unique_values.append(i)
            else:
                while i in unique_values:
                    i -=1
                    print('new value of i is ', i, ' unique_values ', unique_values)
                    total_deletes+=1
                    if i <= 0:
                        break
                            
                unique_values.append(i)
        
        print(total_deletes)
        
        return total_deletes
            
        

                
