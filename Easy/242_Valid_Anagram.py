## LilacDotDev: 5/5/25
# Notes: Attempt to solve a problem in py3

# Using the default python sorted() method which uses
# Timsort algo to do its sorting (which is nlogn)

# Valid Anagram: Quick Once-Lookover (<1 minute)
#   Pseudocode:
#   - If both strings, s and t, sorted are equal to eachother:
#   - return true
#   - Otherwise, they're not anagrams so:
#   - return false

# Time Complexity # All the same since it needs to be sorted no matter what
#   Best: O(n log n)
#   Worst: O(n log n)
#   Average: O(n log n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If sorted string s == sorted string t, return true
        if sorted(s) == sorted(t):
            return True
        # if nothings returned, return false
        return False