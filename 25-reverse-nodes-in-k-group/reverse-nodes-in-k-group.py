# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return None

        curr = head
        prev = None
        Next = None
        count = k

        temp = head
        remainingLen = 0

        while temp:
            temp = temp.next
            remainingLen += 1

        if remainingLen < k:
            return head

        while curr and count > 0:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
            count -= 1

        head.next = self.reverseKGroup(curr, k)
        return prev