# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        i=0
      
        while curr:
            curr=curr.next
            i+=1
        
        i=i-n
        if i==0:
         return head.next
        curr=head
        prev=curr
        for _ in range(i):
            prev=curr
            curr=curr.next
        if curr and prev:
         prev.next=curr.next
        
        return head

        
        

