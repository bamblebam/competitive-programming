class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indices={c:i for i,c in enumerate(nums)}
        for a,b in operations:
            nums[indices[a]]=b
            indices[b]=indices[a]
        return nums