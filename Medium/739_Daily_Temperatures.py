## LilacDotDev: 5/18/25
#   Daily Temperatures: Solved in ~10m with tuple stack logic
#
#   Pseudocode:
#   - Create return array with all 0s and stack array with tuple items [temp, index]
#   - iterate through temperatures with enumerate i, temp
#   - while stack is not empty and temp is greater than the temp of the last item in the stack,
#   - pop the last item in the stack and add i - popped item's index to the popped item in the return array
#   - append temp, i to the stack.
#   - return ret when complete
#
#   Time Complexity:
#   Average: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                sTemp, sIdx = stack.pop()
                ret[sIdx] = i - sIdx
            stack.append((temp, i))
        return ret
    
# -------------=========| Initial Attempt ↓ | Latest Attempt ↑ |=========------------- #

## LilacDotDev: 5/18/25
#   Daily Temperatures: Solved in ~6m w/ double for loop break
#
#   Pseudocode:
#   - Create return array with all 0s
#   - iterate through all items excluding the last in temperatures
#   - iterate from i+1 to the end of temperatures
#   - if x days away there exists a warmer temperature, add x - i distance to ret[i] and break out the loop
#   - otherwise, use the already placed zero and move on
#   - return ret
#
#   Time Complexity:
#   Average: O(n^2)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        
        for i in range(0,len(temperatures)-1):
            for x in range(i + 1, len(temperatures)):
                if temperatures[x] > temperatures[i]:
                    ret[i] = x - i
                    break
        return ret