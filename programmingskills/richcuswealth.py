# 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        
        n = len(accounts)
        for i in range(n):
            total = sum(accounts[i])
            maxwealth = max(total,maxwealth)
            
        return maxwealth