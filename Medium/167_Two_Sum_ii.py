## LilacDotDev: 5/11/25
#   Twosum II: Fast Solution
#
#
#   Pseudocode:
#   - Create pointers i,j at 0 and n
#   - For the length of the array, check if numbers[i]+numbers[j] is either:
#       - less than the target : move leftmost pointer i to be greater (+1)
#       - greater than the target : move rightmost pointer j to be less (-1)
#       - equal to the target : return i+1 and j+1 as an array
#
#   Time Complexity
#   Average: O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        for n in range(1,len(numbers)):
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return ([i+1,j+1])