## LilacDotDev: 5/16/25
#   Min Stack
#   Note: I really liked this one. Using python's native list methods was fun to learn.
#         Plus, having to use self (or this) is very interesting in terms of understanding scope.
#
#   Pseudocode:
#   - init stack with self.stack
#   - append val to end of list for push
#   - use stack.pop method for pop
#   - return stack[-1] for top, returning last element
#   - return min(self.stack) for minimum stack item
#
#   Time Complexity
#   Average: O(1) for each operation

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()