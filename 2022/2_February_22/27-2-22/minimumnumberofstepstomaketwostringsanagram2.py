class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1=Counter(s)
        count2=Counter(t)
        ans=0
        for k,v in count1.items():
            if v>count2[k]:
                ans+=v-count2[k]
        for k,v in count2.items():
            if v>count1[k]:
                ans+=v-count1[k]
        return ans