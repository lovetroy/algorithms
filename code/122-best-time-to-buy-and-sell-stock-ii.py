def max_profit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]
    return profit


def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    valley = prices[0]
    peak = prices[0]
    profit = 0
    i = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i + 1] <= prices[i]:
            i += 1
        valley = prices[i]
        while i < len(prices) - 1 and prices[i + 1] >= prices[i]:
            i += 1
        peak = prices[i]
        profit += peak - valley
    return profit


# def max_profit(prices):
#     def calculate(prices, s):
#         if s > len(prices):
#             return 0
#         max = 0
#         for start in range(s, len(prices)):
#             maxprofit = 0
#             for i in range(start + 1, len(prices)):
#                 if prices[i] > prices[start]:
#                     profit = calculate(prices, i + 1) + prices[i] - prices[start]
#                     if profit > maxprofit:
#                         maxprofit = profit
#             if maxprofit > max:
#                 max = maxprofit
#         return max
#
#     return calculate(prices, 0)


prices = [7, 8, 4, 9]
print(max_profit(prices))
