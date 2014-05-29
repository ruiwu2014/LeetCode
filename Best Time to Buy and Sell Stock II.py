class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        if len(prices)<2:
            return 0
        low = 0
        high = low + 1
        maximal = 0
        while high < len(prices):
            if  prices[low]<prices[high]:
                profit += prices[high]-prices[low]
                low = high
                high = low +1
            else:
                low = high
                high = low +1
        return profit







