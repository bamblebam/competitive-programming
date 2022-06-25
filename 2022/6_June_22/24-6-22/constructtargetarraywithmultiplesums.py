class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """
        https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/1199298/Python-Start-from-the-end-with-heaps-explained
        """
        heap=[-x for x in target]
        heapify(heap)
        s=sum(target)
        
        while True:
            elem=-heappop(heap)
            if elem==1:
                return True
            if elem==s:
                return False
            cand=(elem-1)%(s-elem)+1
            if cand==elem:
                return False
            s-=elem-cand
            heappush(heap,-cand)