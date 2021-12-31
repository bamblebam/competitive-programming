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
    
        # #alternate solution O(n)
        # #use monotone stack
        # #iterate through reverse nums2 and if the curr element is greater than the latest one in the stack pop it. The remaining stack[-1] will be the answer. if stack is empty it is -1.
        # #if number is less than stcak[-1] just add it to stack and its answer is stack[-1]
        # idx_map=dict()
        # stack=list()
        # m,n=len(nums1),len(nums2)
        
        # for i in range(n-1,-1,-1):
        #     curr=nums2[i]
        #     while stack and stack[-1]<curr:
        #         stack.pop()
        #     if not stack:
        #         idx_map[curr]=-1
        #         stack.append(curr)
        #         continue
        #     idx_map[curr]=stack[-1]
        #     stack.append(curr)
        
        # return list(idx_map[x] for x in nums1)