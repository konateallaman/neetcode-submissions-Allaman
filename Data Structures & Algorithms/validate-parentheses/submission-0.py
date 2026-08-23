class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        parenthese_pairs={')':'(','}':'{',']':'['}
        for char in s:
            if char in parenthese_pairs:
                if stack and stack[-1]==parenthese_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack)==0
            
        