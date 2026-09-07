"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        temp = head
        prev = temp

        while temp:
            if temp.child:
                if temp.next:
                    temp.next.prev = None
                    stack.append(temp.next)

                temp.next = temp.child
                temp.child.prev = temp

            prev = temp
            temp = temp.next

        temp = prev
        
        while stack:
            temp.next = stack.pop()
            temp.next.prev = temp

            while temp.next:
                temp = temp.next

        temp = head

        while temp:
            if temp.child:
                temp.child = None

            temp = temp.next
        
        return head