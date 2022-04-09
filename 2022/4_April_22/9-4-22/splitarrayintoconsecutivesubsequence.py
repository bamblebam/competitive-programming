class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        I used a greedy algorithm.
leftis a hashmap, left[i] counts the number of i that I haven't placed yet.
endis a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
Then I tried to split the nums one by one.
If I could neither add a number to the end of a existing consecutive subsequence nor find two following number in the left, I returned False
        """
        left=Counter(nums)
        end=Counter()
        for num in nums:
            if left[num]==0:
                continue
            left[num]-=1
            if end[num-1]>0:
                end[num-1]-=1
                end[num]+=1
            elif left[num+1] and left[num+2]:
                left[num+1]-=1
                left[num+2]-=1
                end[num+2]+=1
            else:
                return False
        return True
                
            