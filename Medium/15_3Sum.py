## LilacDotDev: 5/13/25
#   3Sum
#   This was a tricky one as well. Not too bad with a bit of logic, though!
#   Solved like 2sum ii with two pointers. I had to consult NeetCode for help.
#
#   Edit: Solution changed by shifting l += 1 after a correct answer
#
#   Pseudocode:
#   - Create return set
#   - Sort nums
#   - For target in nums
#   - For i in range target to end
#   - l = i , r = len(nums) - 1
#   - if l is equal to r, break
#   - else if the sum of l and r are less than the target, add 1 to l
#   - else if the sum of l and r are greater than the target, subtract 1 from r
#   - else if the sum of l and r are equal to the target, add [nums[target], nums[l], nums[r]] to the return set
#   - Return set
#
#   Time Complexity
#   Average: O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                triplet = a + nums[l] + nums[r]
                if triplet > 0:
                    r -= 1
                elif triplet < 0:
                    l += 1
                else:
                    ret.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return ret

# ====================== Initial Solution Attempt ====================== #

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Create Return Array
        ret = []
        # Sort nums in n log n
        nums.sort()

        # Loop from 0 -> nums length - 1. Create l = target + 1 to make them distinct,
        # and make r = length - 1, making (i != j & k) & (j != k)
        for target in range(0, len(nums) - 1):
            l, r = target + 1, len(nums) - 1

            # Loop through range target to length - 1 with no repeats.
            # if l == r we know they met and can break out
            # if l+r < target, we add 1 to l to make it larget and vice versa
            # if equal, we check for duplicates and add it to the list.
            for i in range(target + 1, len(nums) - 1):
                if l == r:
                    break
                if nums[l] + nums[r] < abs(nums[target]):
                    l += 1
                elif nums[l] + nums[r] > abs(nums[target]):
                    r -= 1
                elif nums[l] + nums[r] == abs(nums[target]):
                    if [nums[target], nums[l], nums[r]] not in ret:
                        ret.append([nums[target], nums[l], nums[r]])
                    r -= 1
        return ret

