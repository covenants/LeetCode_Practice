class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        b = collections.defaultdict(list)
        
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.':
                    #print(char) 
                    if char in b:
                        for position in b[char]:
                            #print(position)
                            # if the same number exists in the same row
                            # if the same number exists in the same column 
                            # else divide by 3 to find if they are in the same 3X3 (integer division)
                            if (position[0] == x) or (position[1]==y) or ((position[0]//3 == x//3) and (position[1]//3 == y//3)):
                                print(position[0], position[0]//3, position[1], position[1]//3)
                                return False
                    
                    # Then add the position of the character
                    b[char].append((x,y))
                    
        return True
