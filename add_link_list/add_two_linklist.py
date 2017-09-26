# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        if l1 is None: return l2
        if l2 is None: return l1

        head1 = l1
        head2 = l2

        while head1.next is not None or head2.next is not None:
            if head1.next is None:
                head1.next = ListNode(0)
            if head2.next is None:
                head2.next = ListNode(0)

            sumNum = head1.val + head2.val
            if sumNum >= 10:
                head1.val = sumNum
                flag = 1
                head1.next.val += 1
            else:
                head1.val = sumNum
                flag = 0
            head1 = head1.next
            head2 = head2.next
        else:
            head1.val = head1.val + head2.val
            if head1.val >= 10:
                head1.val = head1.val
                head1.next = ListNode(1)
        return l1