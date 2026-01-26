
import os
from Member import Member
from SessionManager import SessionManager
from Menu import Menu


class MemberService:
    def __init__(self,file_name="member.txt"):
        self.file_name = file_name
        self.members = []
        self.menu = Menu()
        self.session = SessionManager()
        self.load_members()

    def load_members(self):

        if not os.path.exists(self.file_name):
            self.save_members()
            return

        self.members = []
        with open(self.file_name,"r",encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))

    def save_members(self):
        with open(self.file_name,"w",encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())

    def find_members(self,uid):
        for member in self.members:
            if member.uid == uid:
                return member
        return None

    def members_add(self):
        print("""
    ╔════════════════════════════════════╗
    ║         MBC 아카데미 회원가입         ║
    ╚════════════════════════════════════╝""")
        uid = input(" ○ 아이디 : ")

        if self.find_members(uid):
            print(" → 중복된 아이디입니다.")
            return

        pw = input(" ○ 비밀번호 : ")
        name = input(" ○ 이름 : ")
        email = input(" ○ 이메일 : ")

        self.members.append(Member(uid,pw,name,email))
        self.save_members()
        self.load_members()
        print(" → 회원가입이 완료되었습니다.")
        self.members_login()

    def members_login(self):
        print("""
    ╔════════════════════════════════════╗
    ║          MBC 아카데미 로그인          ║
    ╚════════════════════════════════════╝""")
        uid = input(" ○ 아이디 : ")
        member = self.find_members(uid)
        pw = input(" ○ 비밀번호 : ")
        if not member:
            print(" → 존재하지 않는 아이디 입니다.")
            return
        if not member.active:
            print(" → 비활성화계정입니다.")
            return

        if member.pw == pw:
            print(f"{member.name}님 안녕하세요!")
            self.session.login(member)
            self.subrun()

    def members_modify(self):
        member = self.session.get_user()
        if member.role =="user":role1 = "학생"
        elif member.role == "professor":role1 = "교수"
        elif member.role == "admin":role1 = "관리자"
        else:role1 = "알수없음"

        print(f"""
    ╔════════════════════════════════════╗
    ║            MBC 마이페이지            ║
    ╚════════════════════════════════════╝
     ○ 이름 | {member.name}
     ○ 아이디 | {member.uid}
     ○ 이메일 | {member.email}
     ○ 권한 | {role1}
    """)

    def members_modify2(self):
        member = self.session.get_user()
        self.members_modify()

        mod =input("""
     → 수정하실 정보를 선택해주세요!
     1. 이름
     2. 이메일
    >>> """)
        if mod == "1":
            name = input(" ○ 이름 : ")
            member.name = name
            self.save_members()
            self.load_members()
            print(" → 이름 변경완료")
        elif mod == "2":
            email = input(" ○ 이메일 : ")
            member.email = email
            self.save_members()
            self.load_members()
            print(" → 이메일 변경완료")
        else:print("입력오류")

    def members_delete(self):
        member = self.session.get_user()
        pw = input("""
     ○ 회원탈퇴를 원하시는 경우 비밀번호를 입력해주세요!
     >>> """)
        if member.pw == pw:
            print("회원탈퇴 완료")
            member.active = False
            self.save_members()
            self.load_members()
            self.session.logout()


    def subrun(self):
        subrun = True
        while subrun:
            if not self.session.is_logged_in():
                print(" → 로그인 후 이용이 가능합니다.")
                return
            member = self.session.get_user()
            if member.role == "user":
                # 학생 메뉴판
                self.menu.user_menu()
                sel = input(">>> ")
                if sel == "1":
                    self.members_modify()
                elif sel == "2":
                    self.members_modify2()
                elif sel == "3":
                    pass  # 성적조회
                elif sel == "4":
                    pass  # 수강과목조회
                elif sel == "5":
                    pass  # 자유게시판
                elif sel == "6":
                    pass  # 자유게시판-글작성
                elif sel == "7":
                    pass  # 자유게시판-내글 관리
                elif sel == "8":
                    self.session.logout()
                    return
                elif sel == "9":
                    self.members_delete()
                elif sel == "0":
                    subrun = False

            elif member.role == "admin":
                self.menu.admin_menu()
                sel = input(">>> ")
                if sel == "1":
                    pass  # 대시보드
                elif sel == "2":
                    pass  # 회원목록조회
                elif sel == "3":
                    pass  # 회원권한관리
                elif sel == "4":
                    pass  # 회원정보수정
                elif sel == "5":
                    pass  # 회원비활성화처리
                elif sel == "6":
                    pass  # 전체성적관리
                elif sel == "7":
                    pass  # 게시판관리
                elif sel == "8":
                    self.session.logout()
                    return
                elif sel == "0":
                    subrun = False

            elif member.role == "professor":
                self.menu.professor_menu()
                sel = input(">>> ")
                if sel == "1":
                    self.members_modify()
                elif sel == "2":
                    self.members_modify2()
                elif sel == "3":
                    pass  # 담당과목관리
                elif sel == "4":
                    pass  # 학생성적입력
                elif sel == "5":
                    pass  # 학생성적조회
                elif sel == "6":
                    pass  # 학생성적수정
                elif sel == "7":
                    pass  # 자유게시판
                elif sel == "8":
                    pass  # 자유게시판 |글 작성
                elif sel == "9":
                    pass  # 자유게시판 |내 글 관리
                elif sel == "0":
                    subrun = False

            else:
                return


