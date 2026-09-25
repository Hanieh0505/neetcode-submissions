class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsss = {}
        countttt = {}
        
        for char in s:
            countsss[char] = countsss.get(char, 0) + 1
        for char in t:
            countttt[char] = countttt.get(char, 0) + 1
        
        return countsss == countttt