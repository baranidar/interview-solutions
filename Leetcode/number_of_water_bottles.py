def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    balance = numBottles
    while balance >= numExchange:
        get = int (balance / numExchange)
        balance = (balance % numExchange) + get
        numBottles += get
        #print(f"get: {get}, balance: {balance}, numBottles: {numBottles}")
    return numBottles
