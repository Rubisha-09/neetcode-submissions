class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                boxes = (r // 3) * 3 + (c // 3)

                if num in row[r] or num in column[c] or num in box[boxes]:
                    return False

                row[r].add(num)
                column[c].add(num)
                box[boxes].add(num)

        return True