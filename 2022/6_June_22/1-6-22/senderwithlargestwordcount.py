class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        c=Counter()
        for msg,sender in zip(messages,senders):
            c[sender]+=len(msg.split())
        max_=0
        ans=None
        for k,v in c.items():
            if v>max_:
                max_=v
                ans=k
            elif v==max_:
                ans=max(k,ans)
        return ans