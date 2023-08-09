class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 행 확인 함수
        def check_row(row_num: int, target: list):
            # 숫자 성분을 넣을 빈 리스트 sheet 생성
            sheet = []
            # 행 리스트 내에서 .이 아닌 성분들을 sheet에 append
            for i in range(9):
                if target[row_num][i] != ".":
                    sheet.append(target[row_num][i])
            # sheet 내의 중복 여부 판단
            if len(sheet) == len(set(sheet)):
                return True
            else:
                return False
        # 열 확인 함수
        def check_col(col_num: int, target: list):
            # 숫자 성분을 넣을 빈 리스트 sheet 생성
            sheet = []
            # 열 리스트 내에서 .이 아닌 성분들을 sheet에 append
            for i in range(9):
                if target[i][col_num] != ".":
                    sheet.append(target[i][col_num])
            # sheet 내의 중복 여부 판단
            if len(sheet) == len(set(sheet)):
                return True
            else:
                return False
        # 서브박스 확인 함수
        def check_subbox(sub_num: int, target: list):
            # 서브박스를 0~8로 네이밍할 경우, 3으로 나눈 몫과 나머지 확인
            # 몫은 board[여기!][], 나머지는 board[][여기!]를 지정
            sub_row = sub_num//3
            sub_col = sub_num%3
            sheet = []
            for i in [sub_row*3, sub_row*3+1, sub_row*3+2]:
                for j in [sub_col*3, sub_col*3+1, sub_col*3+2]:
                    if target[i][j] != ".":
                        sheet.append(target[i][j])
            # 위와 마찬가지로 sheet 내 중복 여부 판단
            if len(sheet) == len(set(sheet)):
                return True
            else:
                return False
        # 이제 그냥 슈루룩 돌리되 중간중간 return 넣어서 바로바로 끝내기
        for i in range(9):
            if not check_row(i, board):
                return False
            if not check_col(i, board):
                return False
            if not check_subbox(i, board):
                return False
        return True