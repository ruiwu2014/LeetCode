# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        #value = head.val
        current = head
        runner = current.next
        while runner:
            if current.val == runner.val:
                current.next = runner.next
                runner = current.next
            else:
                current = runner
                runner = current.next

        return head