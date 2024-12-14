def trap(self, height: List[int]) -> int:
    capacity = 0
    for index, item in enumerate(height):
        # if index == 0 or index == len(height) - 1:
        #     capacity += 0
        i = j = index
        left = right = min_height = 0
        #find tallest to the left
        while i >= 0:
            left = max(left, height[i])
            i -= 1
        #find tallest to the right
        while j < len(height):
            right = max(right, height[j])
            j += 1
        
        min_height = min(left, right)
        volume = min_height - item if item != 0 else min_height
        capacity += volume
    return capacity
