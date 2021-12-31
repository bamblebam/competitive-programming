class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        #iterate through all the words and if it is vowel increase count of counter
        ans=0
        count=defaultdict(lambda:0)
        vowels="aeiou"
        
        for i,x in enumerate(word):
            if x in vowels:
                if not i or word[i-1] not in vowels:
                    jj=j=i
                    count.clear()
                count[x]+=1
                while len(count)==5 and all(count.values()):
                    count[word[j]]-=1
                    j+=1
                ans+=j-jj
        
        return ans
                