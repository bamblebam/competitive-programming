class Solution:
    def isAlienSorted(self, words, order):
        order_map = dict()
        for index, letter in enumerate(order):
            order_map[letter] = index
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    break
        return True

# alternate Solution
# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         idx_map=dict()
#         for i,letter in enumerate(order):
#             idx_map[letter]=i
#         for i in range(1,len(words)):
#             w1=words[i-1]
#             w2=words[i]
#             n1=len(w1)
#             n2=len(w2)
#             i,j=0,0
#             flag=False
#             while i<n1 and j<n2:
#                 char1,char2=w1[i],w2[j]
#                 print(char1,char2)
#                 if idx_map[char1]>idx_map[char2]:
#                     return False
#                 elif idx_map[char1]<idx_map[char2]:
#                     flag=True
#                     break
#                 i+=1
#                 j+=1
#             if not flag and n1>n2:
#                 return False
#         return True