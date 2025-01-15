#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def findMin(nums):

    #array is not rotated
    if nums[0] < nums[-1]:
        return nums[0]

    i = 0
    j = len(nums)-1

    while i < j:
        mid_point = (i+j)//2
        if nums[0] <= nums[mid_point]:
            i = mid_point + 1
        else:
            j = mid_point
    return nums[i]

result = findMin([3,4,5,1,2])
print(result)

'''
0,1,2,3
3,0,1,2

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,9,10,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''