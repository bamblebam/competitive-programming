class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        p=set()
        count=Counter()
        for w,l in matches:
            p.add(w)
            p.add(l)
            count[l]+=1
        return [sorted(list(p-set(count.keys()))),sorted([k for k,v in count.items() if v==1])]