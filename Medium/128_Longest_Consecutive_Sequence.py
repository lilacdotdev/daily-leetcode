## LilacDotDev: 5/11/25
#   Longest Consecutive Sequence
#   Note: My first thought was to sort the array, but the question asks for O(n)
#   Sorting iteself would have been nlogn
#
#   Pseudocode:
#   - Create a set with all items in nums to make them exclusive
#   - For loop through all nums in the newly created set
#   - If n-1 isnt in the set, we know the streak is broken. If it is, count += 1
#   - While n + count is in the hashset, add 1 to count
#   - Set return variable to the larger between count and return var
#   - Return the return variable
#   
#   Time Complexity
#   Average: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        ret = 0

        # Iterate through the set
        for n in hashset:

            # We know it's the start of a new streak if the prev num isnt in the set, and can begin a run
            if (n - 1) not in hashset:
                count = 1
                # Loop while n + count following number is in the set. If it is, add one to the count and try next.
                while (n + count) in hashset:
                    count += 1
                # Returns the bigger number betweek count and ret
                ret = max(count, ret)
        return ret