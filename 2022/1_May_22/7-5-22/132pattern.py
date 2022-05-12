class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        Let us keep evaluate min_list, where min_list[i] = min(nums[0], ..., nums[i]).
Also let us traverse our nums from the end and keep stack with decreasing elements, which are more than min_list[j] for given j.
We will try to find 132 pattern, where nums[j] is middle number in this pattern.

Let us look through the code and see what is going on:

If nums[j] <= min_list[j], there is no need to put this number to stack: it means actually that nums[j] is less than all previous numbers and it can not be the middle element in our 132 pattern.
Now, if nums[j] > min_list[j], we need to keep our stack clean: if we have numbers which are leaa or equal than min_list[j], we remove them from our stack. So, we have now stack[-1] > min_list[j]. If it is also happen, that stack[-1] < nums[j], then we are happy: we found our pattern: we choose stack[-1] for our 2 in pattern, nums[j] for our 3 and element where minumum reached: min_list[j] for our 1: we have our 1 less than 2 and 2 less than 3. In this case we immedietly return True. In the end we append nums[j] to our stack.
If we traversed all list and did not found pattern, we return False.
So, what exaclty will be in our stack on each step?

There always be numbers more or equal than nums[j] inside
Which are going in decreasing order.
Why it will not change on the next step? If our next number (nums[j-1]) is more than top of our stack, we found our 132 pattern! If it is less, then we put it into our stack and decreasing order is satisfied (property s) and if we have top of our stack equal to nums[j-1], so property 1 is also satisfied.

Complexty is O(n), both for time and memory, because we traverse our list twice: once in one direction and once in opposite
        """
        min_list=list(accumulate(nums,min))
        stack=list()
        n=len(nums)
        
        for i in range(n-1,-1,-1):
            if nums[i]>min_list[i]:
                while stack and stack[-1]<=min_list[i]:
                    stack.pop()
                if stack and stack[-1]<nums[i]:
                    return True
                stack.append(nums[i])
        return False