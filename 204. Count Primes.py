class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        
        primes = [2]
        # 1 is not prime, 0 is prime
        for i in range(3, n, 2):
            # Check against all previous saved primes
            for p in primes:
                # 1. if any prime square bigger than current number
                if p * p > i:
                    #print(i, p)
                    primes.append(i)
                    break
                # 2. if current number divisible by any prime, then break (not prime)
                # else try with next prime 
                if i % p == 0:
                    break
                    
        #print(primes)
        
        return len(primes)
                
            
        
