class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count=Counter()
        for c in s:
            if c in target:
                count[c]+=1
        count2=Counter(target)
        for k,v in count2.items():
            count[k]//=v
        return min(count[c] for c in target)