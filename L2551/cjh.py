class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 행 체크
        for i in range(len(board)):
            count = 0
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    count += 1
                
            if len(board[i]) != len(set(board[i])) + count - 1:
                print(board[i])
                return False
                break
        
        # 열 체크
        for j in range(len(board)):
            row = []
            count = 0
            for i in range(len(board[j])):
                row.append(board[i][j])
                if board[i][j] == '.':
                    count += 1
            if len(row) != len(set(row)) + count - 1:
                return False
                break
        
        # 사각형 체크
        s = [0, 3, 6]
        for j in s:
            for i in s:
                count = 0
                square = []
                square += board[i][j:j+3]
                square += board[i+1][j:j+3]
                square += board[i+2][j:j+3]
                for _ in range(len(square)):
                    if square[_] == '.':
                        count += 1
                if len(square) != len(set(square)) + count - 1:
                    return False
                    break
        return True