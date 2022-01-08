class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count=Counter(words)
        ans=0
        seen=set()
        dubs=0
        dubs2=set()

        for word in count:
            x=word[::-1]
            
            if x==word:
                dt=count[x]
                if dt%2:
                    dubs+=dt-1
                    count[x]-=dt-1
                    seen.add(x)
                    dubs2.add(x)
                else:
                    dubs+=dt
                    seen.add(x)
                continue
                
            if word in seen or x in seen:
                continue
            t=min(count[word],count[x])
            seen.add(word)
            seen.add(x)
            ans+=t
            
        odd=0
        for x in dubs2:
            if count[x]==1:
                odd=1
                break
        return ans*4 + dubs*2 +odd*2
        