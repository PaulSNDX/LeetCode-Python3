class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictMap = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in dictMap:
                return dictMap[diff], i
            
            dictMap[nums[i]] = i
