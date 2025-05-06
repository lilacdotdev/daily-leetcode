// LilacDotDev: 5/5/25
// Self-note: Another possible solution could just be sorting the arr 
// and using a sliding window approach.


/* Contains Duplicate: Solution after time (about 18 minutes) 
    Hashset Speed over Memory
    Pseudocode:
    - Create HashSet set
    - for loop from 0 -> nums.length
    - if nums[i] exists in hashset, return true
    - else, add it to the hashset
    - return false
*/

// Time Complexity:
//  Best: O(2+2) // Realistically extremely low probability. [1,1,2]
//  Worst: O(2n+2) // Iterate through each element and insert every element
//  Average: O(n)
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Create Hashset "set"
        HashSet set = new HashSet();

        // For each int i in nums
        for(int i : nums){
            // If element i is within the set, return true
            if(set.contains(i)){
                return true;
            }
            // otherwise, add element i to the set
            set.add(i);
        }
        // If never returned, just return false
        return false;
    }
}

// ---------------------------------------------------- //

/* Contains Duplicate: Quick-look Solution (about 1.5 minutes) 
    Brute Force Method
    Pseudocode:
    - index i is the initial item
    - index j is the comparison item
*/

// Time Complexity:
//  Best: O(1) (Technically lol but realisically rare for idx 0 == idx 1)
//  Worst: O(2n^2)
//  Average: O(n*n/2)

class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Loop through nums.length - 1
        for(int i = 0; i < nums.length - 1; i++){
            // Loop through nums.length - i
            for(int j = i + 1; j < nums.length; j++){
                // If elements at i and j are the same, duplicate spotted.
                if(nums[i] == nums[j]){
                    return true;
                }
            }
        }
        // If the whole array is iterated and nothing is returned,
        // nothing duplicated so return false.
        return false;
    }
}