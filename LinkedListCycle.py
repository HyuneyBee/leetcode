# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        c = head
        n = head.next.next

        while c and n:
            if c == n:
                return True
            else:
                c = c.next
                if n.next is None:
                    return False
                n = n.next.next

        return False
