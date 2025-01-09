#https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    import statistics
    if len(nums1) > 0:
        list1_median = statistics.median(nums1)
    if len(nums2) > 0:
        for item in nums2:
            nums1.append(item)
    list2_median = statistics.median(nums1)
    return list2_median

#---
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    import statistics
    merged = nums1 + nums2
    return statistics.median(merged)

#--- O(log(m+n)
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) == 0:
        return self.find_median(nums2)
    if len(nums2) == 0:
        return self.find_median(nums1)

    merged_array = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2) :
        if nums1[i] < nums2[j]:
            merged_array.append(nums1[i])
            i += 1
        else:
            merged_array.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged_array.append(nums1[i])
        i += 1
        
    while j < len(nums2):
        merged_array.append(nums2[j])
        j += 1

    return self.find_median(merged_array)

def find_median(self, arr):
    if len(arr)%2 == 0:
        mid_point = len(arr)//2 - 1
        return (arr[mid_point] + arr[mid_point + 1]) / 2
    else:
        mid_point = len(arr)//2
        return (arr[mid_point])