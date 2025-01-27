#https://leetcode.com/problems/binary-search/submissions/1521647573/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        mid_index = 0
        mid_number = nums[mid_index]
        
        while left_index <= right_index:
            mid_index = (right_index + left_index) // 2
            mid_number = nums[mid_index]
            if mid_number == target:
                return mid_index

            if target < mid_number:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
                
        return -1