class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        for i in range(32):
            mask=2**i
            if (n // mask) %2:
                count +=1
        return count