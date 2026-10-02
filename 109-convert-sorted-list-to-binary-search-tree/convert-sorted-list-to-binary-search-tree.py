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
        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        def sortedListToBSTUtil(start, end) -> TreeNode | None:
            if start > end:
                return None

            mid = start + (end - start) // 2
            root = TreeNode(arr[mid])

            root.left = sortedListToBSTUtil(start, mid - 1)
            root.right = sortedListToBSTUtil(mid + 1, end)
            return root

        return sortedListToBSTUtil(0, len(arr) - 1)