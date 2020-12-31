class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_diff = float('-inf')
        current_price = float('inf')
        
        for price in prices:
            current_price = min(current_price, price)
            max_diff = max(max_diff, price - current_price)
            
        return max_diff
