class Solution:
    def checkString(self, s: str) -> bool:
        a=False
        for c in s:
            if not a and c=="b":
                a=True
            if a and c=="a":
                return False
        if not a:
            return True
        return True