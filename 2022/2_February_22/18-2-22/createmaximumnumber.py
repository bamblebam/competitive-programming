class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        '''
        using the same idea as remove k digits
        since we need to keep k digits between 2 arrays the remaining can be removed
        use the idea to get arrays a,b for nums1,nums2 with i and k-i elements
        so remove the rest
        then just take the max of all possible cases like 0,k,;1,k-1;2,k-2 and so on
        '''
        def helper(nums,k):
            stack,attempts=list(),len(nums)-k
            for digit in nums:
                while stack and stack[-1]<digit and attempts>0:
                    attempts-=1
                    stack.pop()
                stack.append(digit)
            return stack[:k]
        
        def merge(a,b):
            return [max(a,b).pop(0) for _ in a+b]
        
        return max(merge(helper(nums1,i),helper(nums2,k-i)) for i in range(k+1) if i<=len(nums1) and k-i<=len(nums2))