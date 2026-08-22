class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        deja_vue={}
        for i, num in enumerate(nums):
            le_complement = target-num
            if le_complement in deja_vue:
                return [deja_vue[le_complement],i]
            deja_vue[num]=i
        return []

        