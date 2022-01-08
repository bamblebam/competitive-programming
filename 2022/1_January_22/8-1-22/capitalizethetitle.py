class Solution:
    def capitalizeTitle(self, title: str) -> str:
        x=title.split(" ")
        ans=list()
        for word in x:
            if len(word)<=2:
                ans.append(word.lower())
            else:
                ans.append(word.capitalize())
        return " ".join(ans)