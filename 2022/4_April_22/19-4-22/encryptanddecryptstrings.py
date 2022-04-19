class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.key_to_val={keys[i]:values[i] for i in range(len(keys))}
        self.dic=Counter([self.encrypt(x) for x in dictionary])

    def encrypt(self, word1: str) -> str:
        ans=""
        for c in word1:
            if c not in self.key_to_val:
                return ""
            ans+=self.key_to_val[c]
        return ans

    def decrypt(self, word2: str) -> int:
        return self.dic[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)