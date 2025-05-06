// ## INITIAL ATTEMPT ## //
// Iterative Method: Lilac 5/3/25
/*  Iterate through 1-6 (the possible domino values) until an exception is found.
 *  If 6 straight tiles have aforementioned value 1-6, return it.
 *  If none of these attempts works, it returns -1 as instructed. 
 */

// Time Complexity:
//  Worst: O(7n^2)
//  Best: O(6+6+4)
//  Average: O(n+n^2)

class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        int counter = 0; // Counter to see if j got to the 6th iteration
        int index = 0; // Item to be flipped

        // For loop from 1-6
        for (int i = 1; i < 7; i++) {
            counter = 0; // Reset counter every time the loop begins again

            // Loop through all 6 dominos
            for (int j = 0; j < tops.length; j++) {
                // If neither the top nor bottom of the domino are i, 
                // break out and try again with next i.
                if (tops[j] != i && bottoms[j] != i) {
                    break;
                } else { // Else, successful. Thus, update counter.
                    counter++;
                }
            }
            // If counter ran for all 6 dominos, we know all dominos contain i
            if (counter == 6) {
                index = i;
                break;
            }
        }
        // If i is never correctly returned, then we know it failed. Return -1.
        if(counter == 0){return -1;}
        counter = 0;
        // Iterate through tops and find the amount of flips needed
        for(int i = 0; i < tops.length; i++){
            if(tops[i] != index){
                counter++;
            }
        }

        // If the counter is greater than 3, we know we can flip to the bottom.
        if(counter > 3){
            return (6-counter);
        } else {
            return counter;
        }
    }
}