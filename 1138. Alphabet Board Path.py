# Maintain order L D U R

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        r, c  = 0, 0
        d = {}
        
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        while r < 6:
            while c < 5:
                d[list(board[r])[c]] = [r, c]
                if list(board[r])[c] == 'z':
                    break
                if c == 4:
                    c = 0
                    break
                c +=1
            r +=1

        
        i = 0
        target = list(target)
        
        ans = []
        prev = [0, 0]
        
        while i < len(target):
            
            prev_x, prev_y = prev[0], prev[1]
            cur = d[target[i]]
            cur_x, cur_y = cur[0], cur[1]
            
            diff_x = abs(prev_x - cur_x) 
            diff_y = abs(prev_y - cur_y)

            if prev_y > cur_y:
                ans.append(diff_y * 'L')
            
            if prev_x < cur_x :
                ans.append(diff_x * 'D')
                
            if prev_x > cur_x:
                ans.append(diff_x * 'U')

            if prev_y < cur_y :
                ans.append(diff_y * 'R')
            
            ans.append('!')
            prev = cur
            i +=1
            
        return ''.join(ans)
        
        
