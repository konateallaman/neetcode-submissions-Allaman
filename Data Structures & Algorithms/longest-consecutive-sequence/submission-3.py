class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        num_set = set(nums)
        for i in range(n):
            if nums[i] - 1 not in num_set:
                current = 1
                while nums[i] + current in num_set:
                    current += 1
                count = max(count, current)
        return count

        