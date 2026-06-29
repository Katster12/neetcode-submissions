class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closein={')':'(',']':'[','}':'{'}
        for i in s:
            if i in closein:
                if stack and stack[-1]==closein[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False