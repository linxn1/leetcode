# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preNode = None
        current_node = head
        while current_node != None:
            nextNode = current_node.next
            current_node.next = preNode
            preNode = current_node
            current_node = nextNode
        return preNode

def read(node: ListNode):
    if node == None:
        return
    print(node.val)
    read(node.next)
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
read(node)
print(Solution().reverseList(node))
read(node)

