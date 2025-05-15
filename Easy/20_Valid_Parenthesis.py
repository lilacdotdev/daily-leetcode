## LilacDotDev: 5/15/25
#   Valid Parenthesis
#   Note: This was a good one. Solved in approx. 3 minutes.
#
#   Update: Forgot to check for hanging braces. Added a not list clause to the return.
#
#   Pseudocode:
#   NOTE: I noticed that the ascii characters for (), {}, and [] 
#       are within 3 of themselves, but over 20+ of eachother
#   - Create stack
#   - iterate through each item in str s
#   - if it is (, [, or {, append (push) it into the stack
#   - otherwise, check to see if it is greater than 3 of ascii of the last push
#   - if so, we know it is not the corresponding brace, so return false.
#   - if it's gone through all steps without this, return true.
#
#   Time Complexity:
#   Average: O(n)
#   Just one pass through and an if/elif and we have our solution.
#   Space Complexity is O(n) as well.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif stack:
                if abs(ord(c) - ord(stack[-1])) > 3:
                    return False
                else:
                    stack.pop()
            else:
                return False
            
        return not stack