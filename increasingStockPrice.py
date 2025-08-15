def maxProfit(prices):
    left = 0  # buy
    right = 1  #sell
    max_profit = 0
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit
print(maxProfit([7,1,5,3,6,4]))
