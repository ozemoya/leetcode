# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Make DummyNode
        Set first, second to dummy
        Make for loop to add a gap between first and second node
        while first isn't none 
        advance both nodes
        Make second skip one
        return
        """
        temp = ListNode(val = 0, next = head)
        first = temp
        second = temp

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first, second = first.next, second.next
        second.next = second.next.next
        return temp.next
