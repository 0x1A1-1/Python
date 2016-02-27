'''
Created on Feb 26, 2016
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
@author: Cigarent
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
        while 1:
            if l1:
                cur.val += l1.val
                l1 = l1.next
            if l2:
                cur.val += l2.val
                l2 = l2.next
            if cur.val>=10:
                cur.next = ListNode(1)
                cur.val = cur.val - 10
            elif (l1 or l2):
                cur.next = ListNode(0)
            else:
                break
            cur=cur.next
        return dummy
            
            