## LilacDotDev: 5/14/25
#   Trapping Rain Water
#   Note: I really liked this one! Interesting algo to write!
#
#   Pseudocode:
#   - Create left array of length height
#   - Loop through from Left -> Right, creating entries in array left
#      of the highest past value
#   - Loop again from Left <- Right, making the following comparison:
#      The higher value between 0 and min(left[i], right) - height[i]
#       This is added to the volume, as the minimum between left[i] and
#       right is the bounds where water could collect, and subtracting height[i]
#       removes any lower bounds.
#
#   Time Complexity:
#   Worst: O(2n*4+3)
#   Average: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        
        # Iterate through height and add the highest prev value to left[i]
        for i in range(0, len(height)):
            if i == 0:
                pass
            else:
                left[i] = max(height[i-1], left[i-1])

        # Iterate reversely through height and compare left and right bounds, added to vol
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                vol = 0
                right = 0
            else:
                right = max(height[i+1], right)
                vol += max(min(left[i], right) - height[i], 0)
        
        # Return! Go, Me!
        return vol