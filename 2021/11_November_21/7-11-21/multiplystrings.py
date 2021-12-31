class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        #just iterate throught the nums of the smaller num and multiply it with the nums of the bigger num
        #also add carry and multiply by 10 bi=oth the local and the global num
        if len(nums1)>len(nums2):
            nums2,nums1=nums1,nums2
        n=len(nums1)
        m=len(nums2)
        ans=0
        j=1
        for x in nums1[::-1]:
            x=int(x)
            i=1
            temp=0
            carry=0
            for num in nums2[::-1]:
                t=int(num)*x+carry
                r=str(t)
                if len(r)>1:
                    carry=int(r[:-1])
                else:
                    carry=0
                add=int(r[-1])*i
                i*=10
                temp+=add
            temp+=carry*i
            ans+=temp*j
            j*=10
        return str(ans)