class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices) # Total lenght
        CurrentMin=prices[0] #current min
        profit=0 # profit so far

        for i in range(n):
            CurrentMin=min(CurrentMin,prices[i])  #get the best mininum price
            profit=max(profit,prices[i]-CurrentMin) # max profit
        return profit