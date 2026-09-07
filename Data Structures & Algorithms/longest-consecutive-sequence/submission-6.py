class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current = 1
                while num + current in num_set:
                    current += 1
                count = max(count, current)
        return count

        