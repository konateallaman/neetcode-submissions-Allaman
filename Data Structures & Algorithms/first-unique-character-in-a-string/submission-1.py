class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts={}
        for ch in s:
            counts[ch]=counts.get(ch,0)+1
        for i in range(len(s)):
            if counts[s[i]]==1:
                return i
        return -1
        