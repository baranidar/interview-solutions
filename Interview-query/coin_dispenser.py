#https://www.interviewquery.com/questions/coin-dispenser


def coin_exchange(amount, denominations):
    output = []
    while amount > 0:
        #print(amount, denomination, denominations,output)
        for denomination in denominations:
            if denomination <= amount:
                calc = round(amount // denomination)
                amount = round(amount % denomination,2)
                output.append((denomination,calc))
            else:
                continue
    if amount > 0:
        return None
    else:
        return output

# amount = 14.61
# denominations = [5.0, 2.0, 1.0, 0.50, 0.10, 0.05, 0.01]
amount = 4
denominations = [3,2]
result = coin_exchange(amount, denominations)
print(result)
'''
[(5.0, 2), (2.0, 2), (0.5, 1), (0.1, 1), (0.01, 1)]
'''