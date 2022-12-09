class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joinedLists = nums1 + nums2
        joinedLists.sort()
        length = len(joinedLists)

        if length % 2:
            median = joinedLists[length // 2]
        else:
            median = (joinedLists[length // 2] + joinedLists[length // 2 - 1]) / 2
        
        return median
