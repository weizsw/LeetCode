"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):

    def __init__(self):
        self.visited = {}

    def clone(self, node):
        if node:
            if node in self.visited:

                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]

        return None
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        _old = head
        _new = Node(_old.val, None, None)

        self.visited[_old] = _new

        while _old != None:

            _new.next = self.clone(_old.next)
            _new.random = self.clone(_old.random)

            _old = _old.next
            _new = _new.next

        return self.visited[head]