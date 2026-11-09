# Definition for singly-linked list.
from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev






def main() -> None:
    result = Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    print(result)


if __name__ == "__main__":
    main()