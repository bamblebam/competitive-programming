class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """
        use stack to keep on reducing the list
        """
        stack=list()
        n=len(nums)
        for i,x in enumerate(nums):
            stack.append(x)
            while len(stack)>=2 and gcd(stack[-2],stack[-1])>1:
                stack.append(lcm(stack.pop(),stack.pop()))
        return stack
            