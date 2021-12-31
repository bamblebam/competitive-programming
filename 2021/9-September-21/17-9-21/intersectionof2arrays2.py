class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)<len(nums2):
            nums1,nums2=nums2,nums1
        count1=Counter(nums1)
        count2=Counter(nums2)
        ans=list()
        for k,v in count2.items():
            if k in count1:
                ans.extend([k]*min(v,count1[k]))
        return ans
                