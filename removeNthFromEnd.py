# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        total = 0
        curr = head
        while curr:
            total +=1
            curr=curr.next
        if total==1:
            return 
        pos = total - n
        curr = head
        for i in range(pos-1):
            curr=curr.next
        if n==1:
            curr.next=None
        elif n==total:
            return head.next
        else:
            curr.next= curr.next.next
        return head