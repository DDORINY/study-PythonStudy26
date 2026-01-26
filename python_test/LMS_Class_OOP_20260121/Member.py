
class Member:
    def __init__(self,uid,pw,name,email,role="user",active=True):
        self.uid = uid
        self.pw = pw
        self.name = name
        self.email = email
        self.role = role
        self.active = active

    def to_line(self):
        return f"{self.uid}|{self.pw}|{self.name}|{self.email}|{self.role}|{self.active}\n"

    @classmethod
    def from_line(cls,line):
        uid, pw, name, email, role, active = line.strip().split("|")
        return cls(uid,pw,name,email,role,active=="True")