class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashset = []
        t_hashset = []
        for x in s:
            s_hashset.append(x)
        for y in t:
            t_hashset.append(y)
        s_hashset.sort()
        t_hashset.sort()
        if s_hashset == t_hashset:
            return True
        else:
            return False