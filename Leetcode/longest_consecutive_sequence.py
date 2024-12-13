def longestConsecutive(self, nums: List[int]) -> int:
    max_length = 0
    nums = set(nums)
    for i in nums:
        curr_length = 0
        if i-1 not in nums:
            while i in nums:
                curr_length += 1
                i += 1
            max_length = max(max_length, curr_length)
    return max_length
