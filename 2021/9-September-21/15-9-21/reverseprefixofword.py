class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx=0
        flag=False
        for i,c in enumerate(word):
            if c==ch:
                idx=i
                flag=True
                break
        if not flag:
            return word
        return word[:idx+1][::-1]+word[idx+1:]