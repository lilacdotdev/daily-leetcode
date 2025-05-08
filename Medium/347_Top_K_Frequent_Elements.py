## LilacDotDev: 5/8/25
#   Top k Frequent Elements: Solved in <8m
#   HashMap Approach
#
#   Pseudocode:
#   - Create HashMap and ret Array
#   - For loop through elements in nums, adding to their values in hashmap
#   - Reverse sort hashmap
#   - Find elements in range 1 -> k for hashmap
#   - Add them to ret array
#   - Return ret array of k frequent elements.

#   Time Complexity
#   Average: O(n log n) <- (due to sorted())

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Define Hashmap and Array for later use, using defaultdict(int)
        hashmap = defaultdict(int)
        ret = []
        
        # Increment every number to hashmap by 1
        for n in nums:
            hashmap[n] += 1

        # Reverse sort hashmap
        hashmap = sorted(hashmap, key=hashmap.get, reverse=True)

        # Find k most frequent elements and append to ret
        for i in range(1, k+1):
            ret.append(hashmap[i-1])
        
        # Return ret array of k most frequent elements in nums
        return ret