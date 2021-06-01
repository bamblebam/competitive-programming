class Solution:
    def suggestedProducts(self, products, searchWord: str):
        answer = list()
        temp1 = products.copy()
        temp1.sort()
        for i, char in enumerate(searchWord):
            temp2 = list()
            for word in temp1:
                if len(word) > i and word[i] == char:
                    temp2.append(word)
            temp1 = temp2
            if len(temp1) > 3:
                answer.append(temp1[:3])
            else:
                answer.append(temp1)
        return answer


sol = Solution()
print(sol.suggestedProducts(products=[
      "mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"))
