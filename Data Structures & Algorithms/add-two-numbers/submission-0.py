# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry=0
        dummy=ListNode(-1)
        curr=dummy
        summ=0
        while l1 is not None or l2 is not None:
            summ=0
            summ+=carry
            if l1 is not None:
                summ+=l1.val
                l1=l1.next
            if l2 is not None:
                summ+=l2.val
                l2=l2.next
            
            nn=ListNode(summ%10)
            curr.next=nn
            curr=nn
            carry=summ//10
        
        if carry:
            nn=ListNode(carry)
            curr.next=nn
        return dummy.next

        