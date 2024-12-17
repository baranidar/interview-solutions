def minCostClimbingStairs(self, cost: List[int]) -> int:
    index_to_change = -2
    cost[index_to_change] = min(cost[index_to_change], cost[index_to_change] + cost[index_to_change+1])
    for i in range(-3, -1 * (len(cost)+1),-1):
        cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
    return min(cost[0], cost[1])
