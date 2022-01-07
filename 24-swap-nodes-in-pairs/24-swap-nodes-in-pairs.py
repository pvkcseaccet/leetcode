# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def _helper(head):
            if not head: return head
            if not head.next: return head
            thisNode, nextNode = head, head.next
            thisNode.next = _helper(nextNode.next)
            nextNode.next = thisNode
            return nextNode
            
        tempHead = head
        tempHead = _helper(tempHead)
        return tempHead