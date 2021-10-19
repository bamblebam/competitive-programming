class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_map={x:i for i,x in enumerate(nums2)}
        ans=list()
        for num in nums1:
            flag=False
            for i in range(idx_map[num],len(nums2)):
                if nums2[i]>num:
                    flag=True
                    ans.append(nums2[i])
                    break
            if not flag:
                ans.append(-1)
        return ans