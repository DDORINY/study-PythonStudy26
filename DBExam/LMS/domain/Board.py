class Board:
    def __init__(self,id,title, content,member_id,active=True,writer_name=None,writer_uid=None):
        self.id = id # DB의 PK
        self.title = title
        self.content = content
        self.member_id = member_id #작성자의 고유번호 FK
        self.active = active # 삭제 여부 (boolean)
        # JOIN을 통해 사져올 추가 정보들 (선택사항)
        self.writer_name = writer_name
        self.writer_uid = writer_uid

    @classmethod
    def from_db(cls,row:dict):
        if not row : return None
        return cls(
            id = row.get('id'),
            title = row.get('title'),
            content = row.get('content'),
            member_id = row.get('member_id'),
            active = row.get('active'),  #현재 미구현
            # JOIN 쿼리 시 사용할 이름과 아이디
            writer_name = row.get('name'),
            writer_uid = row.get('uid'),
        )

    def __str__(self): # print(board)로 테스트용
        # 목록 출력 시 보여줄 형식 -> 객체를 문잘열로 변환하여 1줄로 출력!
        writer =self.writer_uid if self.writer_uid else f"ID : {self.member_id}"
        # 작성자의 이름이 있는 경우 작성자의 이름을 writer에 넣고 없으면 아이디(작성자 번호)를 넣는다.
        return f"{self.id:<4} | {self.title:<20}| {writer:<10}"