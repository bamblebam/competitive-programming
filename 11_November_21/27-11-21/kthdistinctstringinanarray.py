class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=Counter(arr)
        pos=0
        for word in arr:
            if count[word]==1:
                pos+=1
            if pos==k:
                return word
        return ""