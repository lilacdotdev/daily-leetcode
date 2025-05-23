## LilacDotDev : 5/22/25
#   Best time to profit
#
#   PseudoCode:
#   - create ret var
#   - low = starting porint
#   - iterate through prices by x
#   - set ret to the max between itself and current item x subtracted by the lowers point low
#   - set the lowest point low to the minimum between item x and itself AFTER to ensure no data deletion or double dipping
#   - return ret when done
#
#   Time Complexity:
#   Average: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        low = prices[0]

        for x in prices:
            ret = max(ret, x - low)
            low = min(low, x)
        return ret