'''
Find subarrays that meet both conditions
1. Index i must be the biggest element in the subarrays, and
2. Subarray start with or end with index i.

Eg: [1,4,5,6,7]
Output: [1,2,3,4,4]
because of the below subarrays
[[1], [4], [5], [6], [7], [1, 4], [4, 5], [5, 6], [6, 7], [1, 4, 5], [4, 5, 6], [5, 6, 7], [1, 4, 5, 6], [4, 5, 6, 7]]
'''

def subarrays(arr):
  # let us populate all combinations inside subset
  subsets = []
  result = []
  for i in range(len(arr)):
    for j in range(len(arr) - i + 1):
      if arr[j: j+i] != []:
        subsets.append(arr[j: j + i])
  # for each item in array
  for item in arr:
    count = 0
    for subset in subsets:
       if item >= max(subset) and item in subset and (subset[0] == item or subset[len(subset)-1] == item):
          count = count + 1
    result.append(count)
  return result
