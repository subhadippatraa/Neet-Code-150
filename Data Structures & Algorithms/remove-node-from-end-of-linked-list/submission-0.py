# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size=0
        temp=head

        while temp is not None:
            size+=1
            temp=temp.next
        
        # remove the head
        if size ==n:
            return head.next
        
        n=n%size
        temp=head
        for i in range(size-n-1):
            temp=temp.next
        
        prev_node=temp
        ntd=temp.next

        if ntd.next is None:
            prev_node.next=None
            return head
        prev_node.next=ntd.next
        ntd.next=None

        return head





        
        
        