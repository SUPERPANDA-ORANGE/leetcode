"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        new = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = new
        while p1 is not None and p2 is not None:
            if p1.val<p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        else:
            if p1 is None:
                p3.next = p2
            else:
                p3.next = p1
        return new.next