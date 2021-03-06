# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        newHead = ListNode(0)
        newHead.next = head
        head = newHead
        current = newHead.next
        while not current and not current.next:
            head.next = current.next
            tmp = head.next.next
            current.next = tmp  
            head.next.next = current
            head = current
            current = current.next
             
        return newHead.next
        