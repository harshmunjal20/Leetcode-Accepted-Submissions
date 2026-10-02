# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev = None
        Next = None

        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        
        return prev