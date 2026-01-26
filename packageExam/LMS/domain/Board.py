class Board:
    def __init__(self,bor_no,title,content,user_name,hits,active=True):
        self.bor_no = bor_no            # 게시글 번호
        self.title = title              # 제목
        self.content = content          # 내용
        self.user_name = user_name      # 작성자
        self.hits = int(hits)           # 조회수
        self.active = active            # 공개와 비공개

    def __str__(self):
        status = "활성" if self.active else "비활성"
        return f"{self.bor_no} | {self.title} | {self.content} |{self.user_name}|{self.hits} |{status}"

    def to_line(self):
        return f"{self.bor_no} | {self.title} | {self.content} |{self.user_name}|{self.hits} |{self.active}\n"

    @staticmethod
    def from_line(line:str):
        bro_no,title,content,user_name,hits,active = line.strip().split("|")
        return Board(
            bor_no = bro_no,
            title = title,
            content = content,
            user_name = user_name,
            hits = int(hits),
            active = (active == "True"))
