import os
from packageExam.LMS.domain import *
from packageExam.LMS.common import Session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "..","data","member.txt")

class MemberService:
    members = []
#############################
    #파일 불러오기 저장하기#
#############################
    @classmethod
    def load(cls):
        cls.members = []
        if not os.path.exists(FILE_NAME):
            cls.save()
            return

        with open(FILE_NAME, "r",encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))

    @classmethod
    def save(cls):
        with open(FILE_NAME, "w",encoding="utf-8") as f:
            for member in cls.members:
                f.write(member.to_line())

#############################
     # 회원관리 서비스 def #
#############################

    @classmethod
    def login(cls): # 회원관리에 로그인
        if Session.is_login():
            print("이미 로그인된 계정입니다.")
            return

        print("""
    -------------------------------
            MBC 아카데미 로그인    
    -------------------------------""")
        uid = input("아이디 :")
        upw = input("비밀번호 :")
        for member in cls.members:
            if member.uid == uid and member.upw == upw:
                Session.login(member)
                print(f"{member.name}님 로그인되었습니다.")
                return

            if member.uid == uid and member.upw != upw:
                print("비밀번호 맞지 않습니다.")
                return

        print("존재하지 않는 아이디입니다.")





    @classmethod
    def logout(cls): # 회원관리에 로그아웃
        print("""
    -------------------------------
            로그아웃되었습니다.    
    -------------------------------""")
        Session.logout()
        return

    @classmethod
    def signup(cls):  # 회원관리에 회원가입
        print("""
    -------------------------------
           MBC 아카데미 회원가입   
    -------------------------------""")
        uid = input("아이디 :")
        for member in cls.members:
            if member.uid == uid:
                print("중복되는 아이디입니다.")
                return

        upw = input("비밀번호 :")
        name = input("이름 :")
        print(f"""
    -------------------------------
    이름 :{name}
    아이디 :{uid}
    권한 : user
    입력하신 회원정보로 회원가입되었습니다.
     """)

        member = Member(uid=uid, upw=upw, name=name,role="user",active=True)
        cls.members.append(member)
        cls.save()

    @classmethod
    def modify(cls):  # 회원관리에 내정보수정
        if Session.is_logout() :
            print("""
    -------------------------------
          로그인 후 이용해주세요!    
    -------------------------------""")
            return
        member=Session.login_member
        print(f"""
    -------------------------------
           MBC 아카데미 내정보    
    -------------------------------
    이름 : {member.name}
    아이디 :{member.uid}
    권한 :{member.role}
    -------------------------------
    1. 이름변경 (개명신청)
    2. 비밀번호 변경
    0. 뒤로 이동""")
        sel = input(">>>")
        if sel == "1":
            name =input("변경 이름 :")
            print("이름이 변경되었습니다.")
            member.name = name
            cls.save()

        elif sel == "2":
            upw = input("변경 비밀번호 :")
            print("비밀번호가 변경되었습니다.")
            member.upw = upw
            cls.save()

        elif sel == "0":return
        else:print("잘못입력되었습니다.")

    @classmethod
    def delete_member(cls):  # 회원관리에 회원탈퇴
        if Session.is_logout():
            print("""
        -------------------------------
              로그인 후 이용해주세요!    
        -------------------------------""")
            return

        print("""
        -------------------------------
               MBC 아카데미 회원탈퇴    
        -------------------------------
        회원탈퇴하시겠습니까?
        → 비밀번호 입력 시 탈퇴처리됩니다.""")
        upw = input(">>>")
        for member in cls.members:
            if member.upw == upw:
                member.active = False
                cls.save()

        print("회원탈퇴되었습니다.\n감사합니다.")


