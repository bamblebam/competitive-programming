# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        ans=dummy
        nodes=list()
        temp=list()
        
        while head:
            if head.val==0:
                nodes.append(sum(temp))
                temp=list()
            else:
                temp.append(head.val)
            head=head.next

        for node in nodes[1:]:
            x=ListNode(node)
            dummy.next=x
            dummy=dummy.next
        
        return ans.next
        