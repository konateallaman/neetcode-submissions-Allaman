class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total %2 !=0:
            return False
        partition=total//2
        dp=[False]*(partition+1)
        dp[0]=True

        for num in nums:
            for s in range(partition,num-1,-1):
                dp[s]=dp[s] or dp[s-num]
        return dp[partition]
        