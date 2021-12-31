class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # find all the permutations and then find the kth one
        return "".join(list(map(str,list(permutations(range(1,n+1)))[k-1])))