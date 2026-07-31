class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        res=0
        lft=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[lft])
                lft+=1
            charset.add(s[r])
            res=max(res,r-lft+1)
        return res
        
        