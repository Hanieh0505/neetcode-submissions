from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            
            j = i
            while j < n and s[j] != '#':
                j += 1
            
            
            if j >= n:
                break
                
            
            length = int(s[i:j])
            
            
            word = s[j+1 : j+1 + length]
            result.append(word)
            
            
            i = j + 1 + length
            
        return result