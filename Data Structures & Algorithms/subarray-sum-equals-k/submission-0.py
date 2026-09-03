class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        running_sum = 0
        count = 0
        for num in nums:
            running_sum += num
            count += prefix_counts.get(running_sum - k, 0)
            prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1
        return count
        