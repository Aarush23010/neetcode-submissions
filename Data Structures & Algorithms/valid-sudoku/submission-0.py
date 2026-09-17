class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
            seen.clear()

        for j in range(9):
            for i in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
            seen.clear()
        
        for row in range(0,9,3):
            for column in range(0,9,3):
                for i in range(row, row+3):
                    for j in range (column, column+3):
                        if board[i][j]==".":
                            continue
                        if board[i][j] in seen:
                            return False
                        else:
                            seen.add(board[i][j])

                seen.clear()
        return True

                
        


