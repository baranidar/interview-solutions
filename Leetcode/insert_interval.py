#https://leetcode.com/problems/insert-interval/description/

def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1],newInterval[1])]
        i += 1
    result.append(newInterval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
output = insert(intervals, newInterval)
print(output)