class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_map=dict()
        words=set()
        ans=""
        n=len(pattern)
        s=list(s.split())
        if n!=len(s):
            return False
        for i in range(n):
            char=pattern[i]
            word=s[i]
            if (word in words and char not in word_map) or (word in words and word_map[char]!=word):
                return False
            if char not in word_map:
                word_map[char]=word
                words.add(word)
                ans+=char
                continue
                
            if word==word_map[char]:
                ans+=char
            else:
                return False
                
        return ans==pattern

            
                
            