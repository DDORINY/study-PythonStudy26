class Board:
    def __init__(self,post_no,author_id,title,content,created_at,updated_at,active=True):
        self.post_no = int(post_no) # 게시글 고유번호
        self.author_id = author_id # 작성자
        self.title = title #제목
        self.content = content #내용
        self.created_at = created_at # 최초 생성시점
        self.updated_at = updated_at # 마지막 수정시점
        self.active = active #비공개여부

    def to_line(self):
        return f"{self.post_no}|{self.author}|{self.title}|{self.content}|{self.created_at}|{self.updated_at}|{self.active}\n"

    @classmethod
    def from_line(cls,line):
        post_no,author,title,content,created_at,updated_at,active = line.strip().split('|')
        active =True if active == "True" else False
        return cls(post_no,author,title,content,created_at,updated_at,active)