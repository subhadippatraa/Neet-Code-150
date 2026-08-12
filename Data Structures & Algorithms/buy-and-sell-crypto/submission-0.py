class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini=prices[0]
        profit=0
        for num in prices:
            mini=min(mini,num)
            profit=max(profit,num-mini)
        return profit

        