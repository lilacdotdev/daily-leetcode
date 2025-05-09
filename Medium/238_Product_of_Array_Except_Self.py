##  LilacDotDev: 5/9/25
#   Product of Array Except Self
#   Solved in ~30m. Tricky Question!   
#
#   Pseudocode:
#   - Create two arrays: prefix and ret
#   - Multiply prev by nums[i] and add to prefix[i]
#   - Multiply aft by prefix[i-1] and add to ret[i]
#   - Return ret
#
#   Time Complexity:
#   Average: O(~2n+3) -> O(n)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create prefix and ret arrays and instatiate with nums.length spaces
        prefix = [0] * len(nums)
        ret = [0] * len(nums)

        # Set prev and aft to 1
        prev = 1
        aft = 1

        # For 0 -> nums.length, set prev to prev * nums[i] and add it to prefix[i]
        for i in range(0, len(nums)):
            prev *= nums[i]
            prefix[i] = prev
        
        # For nums.length -> 0, if i isnt 0, ret[i] = aft * prefix[i-1], if i is 0, ret[i] = aft
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                ret[i] = aft
            else:
                ret[i] = aft * prefix[i - 1]
                aft *= nums[i]
        
        # Return array ret
        return ret