# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def findMiddle(head):
            slow_ptr = head
            prev_ptr = None
            fast_ptr = head

            while fast_ptr and fast_ptr.next:
                prev_ptr = slow_ptr
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

            if prev_ptr:
                prev_ptr.next = None

            return slow_ptr


        if not head:
            return None

        mid = findMiddle(head)
        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

