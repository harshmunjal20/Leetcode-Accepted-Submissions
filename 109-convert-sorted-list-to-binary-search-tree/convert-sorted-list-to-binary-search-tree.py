# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        def sortedListToBSTUtil(head, tail) -> TreeNode | None:
            if head == tail:
                return None

            slow = head
            fast = head

            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next

            root = TreeNode(slow.val)

            root.left = sortedListToBSTUtil(head, slow)
            root.right = sortedListToBSTUtil(slow.next if slow else None, tail)
            return root

        return sortedListToBSTUtil(head, None)