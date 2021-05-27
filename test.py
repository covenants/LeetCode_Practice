class Solution:
    def calculate(self, s: str) -> int:
        
        num, stack, sign = 0, [], "+"
        
        for i in range(len(s)):
            
            # we keep the number in num
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                
            # only when we have a sign we operate on the previous sign
            # for 3+2 <- num = 3 after + sign we add stack.append(3)
            # next num = 2
            # after we have * then 
            if s[i] in "+-*/" or i == len(s) - 1:
                
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                
                # set num to zero, only to be increased in case of consecutive numbers
                # else we set to zero so onle single digits gets operated on
                num = 0
                # sign has previous sign, store current sign to sign
                sign = s[i]
        
        print(stack)
        return sum(stack)


a = Solution()
output = a.calculate("3+2*2")
print(output)
