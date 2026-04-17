class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        box_map = {}

        for i in range(len(board)):
            row_set = set()
            col_set = set()

            for j in range(len(board)):

                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

                if board[i][j] != ".":
                    r = i // 3
                    c = j // 3
                    box_key = (r, c)
                    
                    if box_key not in box_map:
                        box_map[box_key] = set()

                    if board[i][j] in box_map[box_key]:
                        return False

                    box_map[box_key].add(board[i][j])
        
        return True