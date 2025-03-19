

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == 'visited':
                return True
            else:
                head.val = 'visited'
            head = head.next
        return False