from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        result = ListNode(0)
        node = result

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next

        if list1 is not None:
            node.next = list1

        if list2 is not None:
            node.next = list2

        return result.next

def main() -> None:
    result = Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))),
                                      ListNode(1, ListNode(3, ListNode(4))))
    print(result)


if __name__ == "__main__":
    main()