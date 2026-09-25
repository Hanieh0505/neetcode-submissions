class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydic = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in mydic:
                mydic[key].append(word)
            else:
                mydic[key] = [word]
        
        return list(mydic.values())



        