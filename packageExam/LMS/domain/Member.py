#회원관리 객체 만들기
# uid,upw,name,role,active로 구성한다.

class Member:
    def __init__(self, uid,upw,name,role,active = True):
        self.uid = uid              # 아이디
        self.upw = upw              # 비밀번호
        self.name = name            # 이름
        self.role = role            # 권한(user, admin)
        self.active = active        # 계정활성화 여부

    def __str__(self):
        status ="활성" if self.active else "비활성"
        return f"{self.uid}|{self.name}|{self.role}|{status}"

    def to_line(self):
        return f"{self.uid}|{self.upw}|{self.name}|{self.role}|{self.active}\n"

    @staticmethod
    def from_line(line:str):
        uid,upw,name,role,active = line.strip().split("|")
        return Member(
            uid=uid,
            upw=upw,
            name=name,
            role=role,
            active = (active == "True"))

    def is_admin(self):
        return self.role == "admin"
