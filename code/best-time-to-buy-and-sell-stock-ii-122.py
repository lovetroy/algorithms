def max_profit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]
    return profit


def max_profit(prices):
    valley = prices[0]
    peak = prices[0]
    profit = 0
    i = 0
    while i < len(prices) - 1:
        while prices[i + 1] <= prices[i] and (i < len(prices) - 1):
            i += 1
        valley = prices[i]
        while prices[i + 1] >= prices[i] and (i < len(prices) - 1):
            i += 1
        peak = prices[i]
        profit += peak - valley
        # i += 1
    return profit


prices = [7, 6, 4, 3, 1]
print(max_profit(prices))