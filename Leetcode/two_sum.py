#https://leetcode.com/problems/two-sum/
def twoSum(nums, target):
    final_list = []
    length_of_list = len(nums)
    cur_pos = 0
    for i in range(length_of_list-1):
        for j in range(i+1, length_of_list):
            if nums[i] + nums[j] == target:
                final_list.append(i)
                final_list.append(j)
                break
    return final_list

def two_sum_hashmap(nums, target):
    hashmap = {}
    result  = []
    for index, item in enumerate(nums):
        to_find = target - item
        if to_find in hashmap:
            result.append([index, hashmap[to_find]])
        else:
            hashmap[item] = index
    return sorted(result[0])

input = (([2,7,11,15],9), ([3,2,4],6),([3,3],6))

for item in input:
    output = two_sum_hashmap(item[0],item[1])
    print(output)