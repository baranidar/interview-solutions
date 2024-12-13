def twoSum(self, nums: List[int], target: int) -> List[int]:
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
