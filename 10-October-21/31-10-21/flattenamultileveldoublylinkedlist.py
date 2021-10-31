"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    pre=None #global var to keep track of the last visited node
    def flatten(self, head: 'Node') -> 'Node':
        #go through all the nodes if it has child go to child list and add to prev nodes next
        #if there is no child node go for the next node flattening
        if not head:
            return None #if empty node return None
        if self.pre:
            self.pre.next=head #add the global prevs next as curr head
            head.prev=self.pre #heads prev as prevs
        self.pre=head #make the global prev the head since now that is the latest visited node
        nxt=head.next #keep the next of the node
        self.flatten(head.child) #if child flatten it
        head.child=None #put heads child as None
        self.flatten(nxt) #flatten the next node if no child list remmains
        return head