import os
from SessionManager import SessionManager

from Board import Board
class BoardService:
    def __init__(self,file_name="Board.txt"):
        self.file_name = file_name
        self.boards = []
        self.session = SessionManager()
        self.load_boards()

    def load_boards(self):
        if not os.path.exists(self.file_name):
            self.save_boards()
            return
        self.boards = []
        with open(self.file_name,"r",encoding="utf-8") as f:
            for line in f:
                self.boards.append(Board.from_line(line))

    def save_boards(self):
        with open(self.file_name,"w",encoding="utf-8") as f:
            for board in self.boards:
                f.write(board.to_line())

    def boards_add(self):pass # 새글작성
    def boards_add_top(self):pass # 공지글 작성
    def boards_list(self):pass # 게시글 조회
    def boards_list_top(self):pass #공지글
    def boards_member_list(self):pass # 내 글 관리->삭제,수정,비공개변경

