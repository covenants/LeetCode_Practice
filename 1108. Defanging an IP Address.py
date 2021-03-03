class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        i = 0
        
        ip_list = list(address)
        
        result = []
        
        while i < len(ip_list):
            if ip_list[i] != '.':
                result.append(ip_list[i])
            else:
                result.append('[')
                result.append('.')
                result.append(']')
            i +=1
        
        print(result)
        
        return ''.join(result)
