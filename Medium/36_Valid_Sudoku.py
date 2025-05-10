## LilacDotDev: 5/10/25
#   Valid Sudoku - HashMap Solution
#   Note: I was struggling hard with this problem due to having worked with few matrices.
#         I will continue to work on it and better my understanding of matrices.
#
#   Pseudocode:
#   - Create hashset with values in it to let python know its a set
#   - Scan from left to right through rows, checking if the item already exists in hashmap.
#   - If it does, return false. Otherwise, add it to hashmap
#   - Repeat this process from top to bottom for cols.
#   - Scan from 0-9 in orders of 3, creating the pattern 0,3,6.
#   - Add this to a modified row scan from 0-3
#   - If it passes all 3 scans, then return True

#   Time Complexity
#   - Average(n^3) <-- Poor... Will revisit another day with better understanding of matrix logic. Thus far, works though.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = {"init", 1}

        # Scan Left -> Right
        for r in range(0,9):
            hashset.clear()
            for c in range(0,9):
                if board[r][c] == '.':
                    pass
                elif board[r][c] in hashset:
                    print(board[r][c], " found in ", hashset, "for Row", r, "Col", c)
                    return False
                else:
                    hashset.add(board[r][c])

        # Scan Top -> Bottom
        for c in range(0,9):
            hashset.clear()
            for r in range(0,9):
                if board[r][c] == '.':
                    pass
                elif board[r][c] in hashset:
                    print(board[r][c], "found in", hashset, "for Row", r, "Col", c)
                    return False
                else:
                    hashset.add(board[r][c])

        # Scan Squares
        for sqx in range (0,9,3):
            for sqy in range (0,9,3):
                hashset.clear()
                for c in range(0,3):
                    for r in range(0,3):
                        if board[sqx+r][sqy+c] == '.':
                            pass
                        elif board[sqx+r][sqy+c] in hashset:
                            print(board[sqx+r][sqy+c], "found in", hashset, "for Square", sqx, sqy, "Row", sqx+r, "Col", sqy+c)
                            return False
                        else:
                            hashset.add(board[sqx+r][sqy+c])
        return True