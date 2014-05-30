# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            head = l2
            run = l1
        else:
            head = l1
            run = l2
        
        hol = head
        current = hol.next
        while current or run:
            if not current:
                hol.next = run
                break
            if not run:
                hol.next = current
                break
            if current.val <= run.val:
                hol.next = current
                current = current.next
                hol = hol.next
            else:
                hol.next = run
                run = run.next
                hol = hol.next
        return head
