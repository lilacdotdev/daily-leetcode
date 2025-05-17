## LilacDotDev: 5/17/25
#   Evaluate Reverse Polish Notation
#
#   Pseudocode:
#   - Create stack
#   - iterate through tokens
#   - if it's not an operator, push it to the stack
#   - Otherwise, evaluate the last 2 items and the operator and round closest to 0
#   - return the last item in the stack as an integer value
#
#   Time Complexity: 
#   Average: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
            else:
                stack.append(int(eval(f"{stack[-2]}{i}{stack[-1]}")))
                stack.pop(-2)
                stack.pop(-2)
        return int(stack[0])