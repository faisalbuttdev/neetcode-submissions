# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        while curr:
            ahead=curr.next
            if curr.val==val:
                prev.next=ahead
            else:
                prev=curr
            curr=ahead

        return dummy.next