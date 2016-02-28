'''
Created on Feb 28, 2016

@author: Cigarent
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list = []
        dum = curr = ListNode(None)
        while head:
            list.append(head.val)
            head=head.next
        list.sort()
        while list:
            tempNode = ListNode(list[0])
            curr.next =tempNode
            curr = curr.next
            list=list[1:]
        return dum.next
'''my sol exceeding time limit'''