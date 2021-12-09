# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        #iterate through the linked list and keep 2 pointers prev and prev2 which are the last and middle elements
        #for each element if both prev and prev2 exists check if prev is a local minima or maxima
        minhead=head
        ans=list()
        count=0
        prev=None
        prev2=None
        
        while minhead:
            if not prev:
                prev=minhead.val
                minhead=minhead.next
                count+=1
                continue
            if not prev2:
                prev2=prev
                prev=minhead.val
                minhead=minhead.next
                count+=1
                continue
            curr=minhead.val
            if prev<curr and prev<prev2:
                ans.append(count-1)
            if prev>curr and prev>prev2:
                ans.append(count-1)
            prev2=prev
            prev=curr
            minhead=minhead.next
            count+=1
            
        if len(ans)<2:
            return [-1,-1]
        
        return [min([ans[i+1]-ans[i] for i in range(len(ans)-1)]),ans[-1]-ans[0]]
        
            