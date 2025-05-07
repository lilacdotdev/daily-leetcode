## LilacDotDev: 5/6/25
#   Two Sum - A Classic! Now solving in Python
#
#   Dictionary/Map Solution
#   
#   Pseudocode:
#   - Sort the nums array
#   - Make a pointer on index 0 and the last element
#   - If i + j is less than target, move i right. otherwise, move j left
#
#   Time Complexity
#   Average: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictmap = {} # Dictionary holding {Value : Index}

        # For loop through nums using enumerate -> (idx, value)
        for i, n in enumerate(nums):
            # Distance of n from target
            remainder = target - n
            # If another item can be found to fill the remainder, return idxes
            if remainder in dictmap:
                return [dictmap[remainder], i]
            # Else add the value as a key and the index as a value to the map
            dictmap[n] = i


#   Sorting Attempt
#   Note: Failiure due to not realizing that the indexes get jumbled too on sort.
#   Would work on Two Sum II, though.
#   
#   Pseudocode:
#   - Sort the nums array
#   - Make a pointer on index 0 and the last element
#   - If i + j is less than target, move i right. otherwise, move j left
#
#   Time Complexity
#   Average: O(n log n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        nums.sort()
        
        while(True):
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return [i,j]