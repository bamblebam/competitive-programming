class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        use backtracking to generate all the permutations
        use a counter to keep track of the number of different digits
        then use 1 and pop and continue
        """
        ans=list()
        n=len(nums)
        
        def helper(path,counter):
            if len(path)==n:
                ans.append(path[:])
                return
            for num in counter:
                if counter[num]>0:
                    counter[num]-=1
                    helper(path+[num],counter)
                    counter[num]+=1
        
        helper([],Counter(nums))
        return ans