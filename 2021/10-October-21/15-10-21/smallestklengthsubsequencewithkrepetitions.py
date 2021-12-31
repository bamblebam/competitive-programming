class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n=len(s)
        c=collections.defaultdict(collections.deque)
        ans=list()
        last=-1
        for i,x in enumerate(s):
            c[x].append(i)
        
        for i in range(k):
            for t in string.ascii_lowercase:
                while c[t] and c[t][0]<last: # remove all letters prior to idx last
                    c[t].popleft()
                
                if c[t] and n-c[t][0]>=k-i: #check if the chosen idx leaves enough space for the remaining letters .i.e. there are enough  letters left
                    cleft=len(c[letter])-bisect.bisect_left(c[letter],c[t][0]) #how much of the required letter is left
                    cond=(k-i>repetition and t!=letter) or (k-i>=repetition and t==letter) #check if enough space is left for required letter after considering the curr letter
                    if cleft>=repetition and cond:
                        last=c[t][0]
                        c[t].popleft()
                        ans.append(t)
                        if letter==t:
                            repetition-=1
                        break
        return "".join(ans)