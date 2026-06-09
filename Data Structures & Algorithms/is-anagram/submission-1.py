class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        counts, countt={},{}

        for _ in range (len(s)):
            counts[s[_]]=1+ counts.get(s[_],0)
            countt[t[_]]=1+ countt.get(t[_],0)
        for i in counts:
            if counts[i] != countt.get(i,0):
                return False

        return True

        