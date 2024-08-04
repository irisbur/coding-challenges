def max_profit(prices):
    profit = 0
    min_val = 2 ** 62
    for i in range(len(prices)):
        if prices[i] < min_val:
            min_val = prices[i]
        elif prices[i] - min_val > profit:
            profit = prices[i] - min_val
    return profit
