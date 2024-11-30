  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      import statistics
      if len(nums1) > 0:
          list1_median = statistics.median(nums1)
      if len(nums2) > 0:
          for item in nums2:
              nums1.append(item)
      list2_median = statistics.median(nums1)
      return list2_median

---
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
     import statistics
      merged = nums1 + nums2
      return statistics.median(merged)
