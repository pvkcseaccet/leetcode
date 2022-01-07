# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        count, kthNodePtr = 1, head
        while count < k: kthNodePtr, count = kthNodePtr.next, count + 1
        kthNode = kthNodePtr
        
        kthNodeFromLast = head
        while kthNodePtr.next != None: kthNodePtr, kthNodeFromLast = kthNodePtr.next, kthNodeFromLast.next
        kthNode.val, kthNodeFromLast.val = kthNodeFromLast.val, kthNode.val
        return head