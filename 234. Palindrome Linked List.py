# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
#put each value in the string
#rever the sting check if it equals to the original string
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
