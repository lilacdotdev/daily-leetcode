## LilacDotDev: 5/19/25
#   Reverse Linked List
#
#   Pseudocode:
#   - Create vars to start at head
#   - While current isn't null, execute shuffle on current node
#   - Temp var becomes the current next pointer
#   - Current next pointer becomes the previous item
#   - Previous becomes the current item
#   - Current becomes the next item
#   - Then we return the previous variable upon breaking out the loop
#
#   Time Complexity:
#   Average: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        # temp var holds the next, next becomes the previous, 
        # previous becomes current, and current becomes the temp
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        # Because loop breaks upon null, we return the last non-null, previous.
        return previous