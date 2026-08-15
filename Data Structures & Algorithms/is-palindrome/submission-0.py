class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        def recu(A,i,j):
            if i>=j:
                return True
            if A[i] != A[j]:
                return False
            return recu(A,i+1,j-1)
        return recu(cleaned,0,len(cleaned)-1)