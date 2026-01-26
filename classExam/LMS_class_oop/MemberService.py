# Member 객체를 CRUD 기능을 넣는다.
# 메뉴 규현
# txt파일 처리 (파일읽기, 파일저장)
# 회원가입 # 로그인 # 로그아웃 # 회원정보수정 # 회원탈퇴
import os

from Member import Member # 회원객체 추가연결
# 사용법 member = Member() → 객체가 생성
#       member.필드/메서드 = ???

class MemberService :
    def __init__(self,file_name="members.txt") :
        self.file_name = file_name
        self.members = [] # 회원들을 리스트로 만들어 Member()객체를 담는다.
        self.session = None # 로그인상태담당 (members의 인덱스 보관용)
        self.load_members() # 아래쪽에 메서드를 호출

    def run(self):
        run=True
        while run:
            self.main_menu()
            sel =input(">>>")

            if sel == "1" : self.member_add()
            elif sel == "2" : self.member_login()
            elif sel == "3" : self.member_logout()
            elif sel == "4" : self.member_modify()
            elif sel == "5" : self.member_delete()
            elif sel == "9" : run = False
            else:
                print("잘못 입력되었습니다.")


    #파일 불러오기 (초기화)
    def load_members(self) : # 파일에서 메모리로 불러온다.
        if not os.path.exists(self.file_name):
            self.save_members()
            return
        self.members = [] # 메모리에 남은 값을 초기화

        with open(self.file_name,"r",encoding="utf-8") as f:
            for line in f :
                self.members.append(Member.from_line(line))
                #                   Member 객처에 .from_line()메서드 실행
                #                                 1줄을 가져와 클래스로 만듬
                # members 리스트에 뒷부분에 추가

    # 파일 저장용 코드
    def save_members(self):
        with open(self.file_name,"w",encoding="utf-8") as f:
            for member in self.members :
                f.write(member.to_line())
                # Member 객체의 메서드를 사용하여 1줄 씩 기록

    def main_menu(self):
        print("""
====================================
   회원관리 프로그램 (member 객체기반)
   
    1. 회원가입
    2. 로그인
    3. 로그아웃
    4. 회원정보수정
    5. 회원탈퇴
====================================
    9. 종료
   """)

    # 아이디를 이용해 members에서 찾는 공통메서드
    def find_member(self, uid):
        for member in self.members : # members 리스트에서 1개씩 member객체를 가져와
            if member.id == uid :   # 가져온 member객체.id와 입력받은 id가 같은가?
                print(member.name, "님을 찾았습니다.")
                return member        # 같은게 있으면 member 객체를 리턴

        return None                  # 없는 경우 None으로 리턴

    def member_add(self):
        print("\n[회원가입]")
        uid =input("아이디 : ")

        if self.find_member(uid): # 자주쓰는 중복코드로 메서드 처리함!
            print("[이미 존재하는 아이디]")
            return

        pw =input("비밀번호 : ")
        name = input("이름 : ")
        role = "user"

        self.members.append(Member(uid,pw,name,role))
        #                   Member 클래스의 init 메서드로 바로 들어가 객체 생성
        self.save_members()
        self.load_members()
        print("[회원가입완료]")

    def member_login(self):
        print("\n[로그인]")

        uid = input("아이디 : ")
        pw = input("비밀번호 :")

        member = self.find_member(uid) # 찾은 아이디객체의 비밀번호를 찾아야함

        if not member:
            print("존재하지 않는 아이디")
            return
        if not member.active:
            print("비활성화 계정")
            return


        if member.pw == pw :
            print(f"{member.name}님 [로그인성공]")
            self.session = member
            
            if member.role == "admin" :
                self.member_admin()                 #   관리자용 메서드
            
        else:
            print("비밀번호 오류")



    def member_logout(self):
        self.session = None
        return

    def member_modify(self):
        if self.session is None:
            print("로그인 후 이용가능")
            return

        print("\n[회원정보수정]")
        member = self.session
        status = "활성" if member.active else "비활성"
        print(f"""
====================================
 이름 : {member.name}
 권한 : {member.role}
 상태 : {status}
 
 ▶ 이름을 변경하시겠습니까? [1]
 ▶ 비활성화 처리하시겠습니까? [2] """)

        sel = input(">>> ")
        if sel == "1" :
            member.name =input("이름 변경:")
            print(f"이름이 {member.name}로 변경완료")
            self.save_members()
            self.load_members()
        elif sel == "2" :
            member.active = False
            print("비활성화 처리완료")
            self.save_members()
            self.load_members()
        else:
            print("입력오류")

    def member_delete(self):
        if self.session is None:
            print("로그인 후 이용가능")
            return
        member = self.session
        self.members.remove(member)
        print("회원탈퇴 처리완료")
        self.save_members()
        self.load_members()


        # ----------------------------------------------------------------------------------------------------------------------
#   관리자 메뉴
    # role ="admin"인 경우 진입이 가능한 메서드
    def member_admin(self):
        subrun =True
        while subrun:
            print("""
====================================
     회원관리 프로그램 (관리자메뉴)
     
     1. 회원 리스트 조회
     2. 비밀번호 변경
     3. 블랙리스트 처리
     4. 권한 변경
====================================
    9. 종료""")
            sel =input(">>>")
            if sel == "1" : self.show_member_lidt()
            elif sel == "2" :
                uid = input("대상 아이디: ")
                member = self.find_member(uid)

                if member:
                    member.pw = input("비밀번호 변경: ")
                    self.save_members()
                    self.load_members()
                    print("비밀번호 변경완료")

                else:
                    print("미등록 아이디")

            elif sel == "3" :
                uid = input("대상 아이디: ")
                member = self.find_member(uid)

                if member:
                    active = input("비활성화 하시겠습니까? \n1.비활성화  2.활성 \n>>>")
                    if active == "1" :
                        member.active = False
                        self.save_members()
                        self.load_members()
                        print("블랙리스트 처리완료")
                    elif active == "2" :
                        member.active =True
                        self.save_members()
                        self.load_members()
                        print("정상회원 처리완료")
                    else:
                        print("입력오류")

                else:
                    print("미등록 아이디")

            elif sel == "4" :
                uid = input("대상 아이디: ")
                member = self.find_member(uid)

                if member:
                    role = input("권한설정 하시겠습니까? \n1.관리자  2.학생\n>>> ")

                    if role == "1":
                        member.role = "admin"
                        self.save_members()
                        self.load_members()
                        print("관리자 설정완료")

                    elif role == "2":
                        member.role = "user"
                        self.save_members()
                        self.load_members()
                        print("학생 설정완료")
                    else:
                        print("입력오류")

                else:
                    print("미등록 아이디")
            elif sel == "9" :subrun = False

    def show_member_lidt(self):
        print("\n[회원목록]")
        print("-"*60)
        print(f"{'ID':10}{'이름':10}{'권한':10}{'상태'}")
        print("-" * 60)

        for member in self.members :
        # members 리스트에 있는 객체를 하나씩 가져와 member에 넣음
            status ="활성" if member.active else "비활성"
            # member.active == True이면 status 변수에 "활성"을 넣고 아니면 "비활성"
            print(f"{member.id:10}{member.name:10}{member.role:10}{status}")
            #                                                      ㄴ "활성" or "비활성"
        print("-" * 60)





