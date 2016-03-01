# Definition for singly-linked list.
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return 
        if not head.next  and k==1:
            return head
        newDum = ListNode(None)
        curr = head
        count = 0
        while curr.next:
            count+=1
            curr = curr.next
        count += 1
        if count == k :
            return head
        elif k>count:
            k = k%count
        curr.next = head
        pos = count - k - 1 
        for i in range(pos):
            head=head.next
        newDum.next = head.next
        head.next = None
        return newDum.next