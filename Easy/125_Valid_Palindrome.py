## LilacDotDev : 5/12/25
#   Valid Palindrome ~ 7m
#   This was a fun one! Came up with what i think is a clever solution using regex despite my hate for it lol
#
#   Update: Solution gave wrong answer for one trial. I failed to understand that alphanumeric contained numeric
#           (whoops lol)
#
#   Pseudocode:
#   - Update s to contain the regex subsituted value of s.lower() with all non a-z characters replaced by ''
#   - Iterate through 0 -> half of the string's length rounded down 
#       (in case of uneven value, the middle will always be the same)
#   - If the mirrored value of i is not equal, then we know they arent the same, so return False
#   - If all mirrored values are the same, the for loop will have completed, so return True
#
#   Time Complexity:
#   Average: O(~ n / 2) -> O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use Regex bounds ^a-z and replace with '' (delete) from s.lower()
        s = re.sub(r'[^a-z0-9]','',s.lower())

        # Iterate through half the length of s and check if mirrored sides are equivalent
        for i in range(0, floor(len(s) / 2)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True