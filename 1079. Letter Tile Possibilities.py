from itertools import combinations, permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        if len(tiles) == 0:
            return 0
        
        if len(tiles) == 1:
            return 1

        master_list = []
        
        x = tiles
        output = [''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]
        
        for t_ in list(set(output)):   
            perm = [''.join(p) for p in permutations(t_)]
            master_list.extend(perm)
        
        return len(list(set(master_list)))
        
