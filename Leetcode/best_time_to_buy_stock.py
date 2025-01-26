#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
def maxProfit(prices):
    profit = 0
    min_price = 0
    i = 0
    j = 1
    while i < len(prices):
        while j < len(prices):
            buy = prices[i]
            sell = prices[j]
            profit  = max(profit,sell-buy)
            j += 1
        i += 1
        j = i + 1
    return profit


def maxProfit_alt(prices):
    if len(prices) == 0:
        return 0
    profit = 0
    buy = prices[0]
    i = 0
    for i  in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
            continue
        profit  = max(profit,prices[i]-buy)
    return  profit

prices  = [7,2,6,1,5,4]
output =  maxProfit_alt(prices)
print(output)


