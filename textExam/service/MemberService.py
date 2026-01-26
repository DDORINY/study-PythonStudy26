import os
from textExam.domain.Member import Member
from textExam.common.Session import Session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "..","data","members.txt")

class MemberService:
    members = []

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

    @classmethod
    def member_add(cls):
        print("""
=====================================
       MBC 아카데미 LMS 회원가입
-------------------------------------
MBC 아카데미 회원가입 창입니다.
회원가입 정보를 입력해주세요!
""")
        uid=input("아이디 : ")
        for member in cls.members:
            if member.uid == uid:
                print("중복된 아이디 입니다.\n다시입력해주세요!")
                return

        pw=input("비밀번호 : ")
        name=input("이름 : ")
        role = "user"

        print(f"""
-------------------------------------
입력하신 회원정보입니다.
이름 : {name}
아이디 : {uid}
권한 : {role}
회원가입하시겠습니까?
[1] YES  [2] NO """)
        sel=input(">>> ")
        if sel == "1":
            print(f"{name}님 회원가입이 완료되었습니다.\n감사합니다.")
            member=Member(uid=uid,pw=pw,name=name,role=role,active=True)
            cls.members.append(member)
            cls.save()

        elif sel == "2":print("회원가입이 취소되었습니다.")
        else:
            return


    @classmethod
    def login(cls):
        if Session.is_login():
            print("이미 로그인되어있습니다.")
            return

        print("""
=====================================
         MBC 아카데미 LMS 로그인
-------------------------------------
MBC 아카데미 로그인 창입니다.
아이디와 비밀번호를 입력해주세요.""")
        uid =input("아이디 : ")
        pw=input("비밀번호 : ")
        for member in cls.members:
            if member.uid == uid and member.pw == pw:
                print(f"{member.name}님 로그인되었습니다.")
                Session.login(member)
                return
            elif member.uid == uid and member.pw != pw:
                print("비밀번호가 맞지 않습니다.")
                return

        print("없는 아이디입니다.")



    @classmethod
    def logout(cls):
        print("""
=====================================
           로그아웃되었습니다
=====================================
""")
        Session.logout()

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요!")
            return

        member = Session.login_member
        print(f"""
=====================================
      MBC 아카데미 LMS 마이페이지
-------------------------------------
MBC 아카데미{member.name}님의 마이페이지입니다.
아이디 : {member.uid}
이름 :{member.name}
권한 : {member.role}
-------------------------------------
[1] 내정보수정  [2] 이전페이지""")
        sel=input(">>> ")
        if sel == "1":
            print("""
-------------------------------------
MBC 아카데미 내정보 수정페이지입니다.
[1] 이름변경 [개명신청]
[2] 권한변경 [관리자 변경 코드 : 1004]
            """)
            sel1=input(">>> ")
            if sel1 == "1":
                name = input("개명신청 : ")
                print(f"{member.name}에서 {name}으로 변경되었습니다.")
                member.name=name
                cls.save()


            elif sel1 == "2":
                role_no=input("관리자 코드를 입력해주세요!\n>>> ")
                if role_no == "1004":
                    print("관리자로 변경되었습니다.")
                    member.role = "admin"
                    cls.save()

                else:print("관리자코드가 맞지않습니다.")
            else:return

        elif sel == "2":return
        else:
            return

    @classmethod
    def del_member(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요!")
            return

        member = Session.login_member
        print(f"""
=====================================
 MBC 아카데미 LMS 회원탈퇴 페이지입니다.
-------------------------------------
비밀번호를 입력해주시면,
회원탈퇴됩니다.
-------------------------------------""")
        pw_del=input(">>> ")
        if member.pw == pw_del:
            print("탈퇴되었습니다. 감사합니다.")
            member.active=False
            cls.save()
        else:return

    @classmethod
    def admin_member(cls):
        if not Session.is_admin():
            print("관리자 메뉴입니다.\n관리자아이디로 로그인 후 이용해주세요!")
            return
        while True:

            print(f"""
=====================================
   MBC 아카데미 LMS 관리자 메뉴입니다.
-------------------------------------
[1] 회원정보조회
[2] 블랙리스트처리
[3] 권한변경
[4] 로그아웃
-------------------------------------
[0] 이전페이지로 이동
=====================================
""")
            sel=input(">>> ")
            if sel == "1":
                print("""
=====================================
       MBC 아카데미 회원정보조회
-------------------------------------""")
                for member in cls.members:
                    print(f"""
이름: {member.name} |아이디 : {member.uid} |권한 : {member.role} |상태 :{member.active}""")
            elif sel == "2":
                print("""
=====================================
       MBC 아카데미 블랙리스트처리
-------------------------------------""")
                uid = input("대상아이디 : ")
                for m in cls.members:
                    if m.uid == uid:
                        if m.active:
                            print(f"{m.name}님을 블랙리스트로 처리되었습니다.")
                            m.active=False
                            cls.save()
                        else:
                            print(f"{m.name}님을 블랙리스트가 [해지]처리되었습니다.")
                            m.active=True
                            cls.save()


            elif sel == "3":
                print("""
=====================================
       MBC 아카데미 권한변경처리
-------------------------------------""")
                uid = input("대상아이디 : ")
                for m in cls.members:
                    if m.uid == uid:
                        if m.role == "user":
                            print(f"{m.name}님을 [admin]로 변경되었습니다.")
                            m.role="admin"
                            cls.save()
                        else:
                            print(f"{m.name}님을 [user]로 변경되었습니다.")
                            m.role="user"
                            cls.save()

            elif sel == "4":
                Session.logout()
                return
            elif sel == "0":break
            else:return






