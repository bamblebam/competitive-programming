class Solution:
    def digitCount(self, num: str) -> bool:
        c=Counter(num)
        for i,x in enumerate(num):
            if c[str(i)]!=int(x):
                return False
        return True