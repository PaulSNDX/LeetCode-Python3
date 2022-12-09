# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], bonus=-1) -> Optional[ListNode]:
        if l1.next == None and l2.next == None and not l1.val and not l2.val:
            if bonus == - 1: return ListNode(0)
            if not bonus: return None

        l3 = ListNode(0)
        temp = l1.val + l2.val + (bonus if bonus > 0 else 0)
        l3.val = temp % 10

        l1 = l1.next if l1.next != None else ListNode(0)
        l2 = l2.next if l2.next != None else ListNode(0)
        l3.next = self.addTwoNumbers(l1, l2, bonus=temp // 10)

        return l3
