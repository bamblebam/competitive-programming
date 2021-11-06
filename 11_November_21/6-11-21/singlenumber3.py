class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #use XOR to sum all elements, duplicates will cancel each other out.
        #then take the lowest set bit and add all elems that have that bit set, that will give num1
        #num1 XOR og result will give num2
        x1=x2=0
        for num in nums:
            x1^=num
        for i in range(32):
            if x1&1<<i:
                break
        for num in nums:
            if num&1<<i:
                x2^=num
        return x2,x1^x2