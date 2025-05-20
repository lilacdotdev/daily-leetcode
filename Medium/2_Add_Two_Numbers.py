## LilacDotDev: 5/20/25
#   Add Two Numbers
#
#   Pseudocode:
#   - Iterate through l1 and arrange as int
#   - Complete the same for L1
#   - Reverse sum
#   - for loop through length of string of sum
#   - typcast to int and direct pointers
#   - return the head
#
#   Time Complexity:
#   Average: O(3n) -> O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2, count = [0, 0, 1]
        while l1:
            t1 += l1.val * count
            count *= 10
            l1 = l1.next
        
        count = 1
        while l2:
            t2 += l2.val * count
            count *= 10
            l2 = l2.next
        
        count = (str)(t1 + t2)
        count = count[::-1]

        head = ListNode(val = int(count[0]))
        prev = head
        for i in range(1, len(count)):
            current = ListNode(val = int(count[i]))
            prev.next = current
            prev = current
        
        return head
