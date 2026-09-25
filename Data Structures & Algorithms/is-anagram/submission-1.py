class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = {}
        c_t={}
        for kalame in s:
            c_s[kalame] = c_s.get(kalame,0) + 1
        for kalame in t:
            c_t[kalame] = c_t.get(kalame, 0) + 1
        
        return c_s == c_t