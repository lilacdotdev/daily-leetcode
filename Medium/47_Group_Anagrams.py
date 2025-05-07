## LilacDotDev: 5/7/25
#   Group Anagrams: HashMap Solution
#
#   Pseudocode:
#   - Create a Hashmap with defaultdict(list)
#   - for every element in strs, create an empty static array of 26 elements
#   - then for every character in the given element s, count the amount of instances of each character
#   - add key: az value: s to return hashmap
#   - return the values of ret hashmap as a list
#
#   Time Complexity
#   Average: O(mn) (where m is length of items in strs and n is len of strs)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a HashMap to be returned at the end
        ret = defaultdict(list)
        # For every s in strs, create new array az with 26 elements (a->z)
        for s in strs:
            az = [0] * 26
            # For every character in s, increment its az value by 1 showing it has x characters c
            for c in s:
                az[ord(c) - ord('a')] += 1
            # Add value s to key az
            ret[tuple(az)].append(s)
        # return a list of all values in HashMap ret
        return list(ret.values())

