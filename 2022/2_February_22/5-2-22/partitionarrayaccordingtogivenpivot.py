class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=list()
        more=list()
        same=list()
        for num in nums:
            if num==pivot:
                same.append(num)
            elif num<pivot:
                less.append(num)
            else:
                more.append(num)
        return less+same+more