## LilacDotDev : 5/21/25
#   Longest Substring
#
#   Time Complexity:
#   Average: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        pointer = 0
        ret = 0

        for x in range(len(s)):
            while s[x] in chars:
                chars.remove(s[pointer])
                pointer += 1
            chars.add(s[x])
            ret = max(ret, x - pointer + 1)
        return ret