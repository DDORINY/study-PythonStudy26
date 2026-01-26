# 회원에 관한 CRUD 를 구현
# 부메뉴와 함께 run() 메서드를 진행

class MemberService:
    def __init__(self):
        # 클래스 생성시 필요한 변수들....
        self.members = []  # 모든 회원이 들어 있는 2차원 리스트
        self.ids = []
        self.pws = []
        self.names = []
        self.emails = []
        self.roles = []
        self.active = []
        self.session = None

    def run(self):
        # 부메뉴 구현 메서드
        subrun = True
        while subrun:
            print("""
-----------------------------------------
             회원관리 프로그램
-----------------------------------------
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 회원서비스 종료

""")
            subSelect = input(">>>")
            if subSelect == "1":
                print("회원가입 메서드 호출")
                self.member_join()

            elif subSelect == "2":
                print("로그인 메서드 호출")
                self.login()

            elif subSelect == "3":
                print("로그아웃 메서드 호출")
                self.logout()

            elif subSelect == "4":
                print("회원정보수정 메서드 호출")
                self.member_update()

            elif subSelect == "5":
                print("회원탈퇴 메서드 호출")
                self.member_delete()

            elif subSelect == "9":
                print("회원서비스 종료 메서드 호출")
                subrun = False

            else:
                print("잘못된 메뉴를 선택하였습니다. ")

    ##########
    # 회원가입 #
    ##########
    def member_join(self):
        print("\n[회원가입]")

        uid = input("아이디: ")
        if uid in self.ids:
            print("이미 존재하는 아이디입니다. ")
            return

        pw = input("비번: ")
        name = input("이름: ")
        email = input("이메일: ")

        print("""
\n[권한선택]
1. 관리자
2. 교수
3. 학생        
""")
        role_choice = input("선택: ")
        if role_choice == "1":
            role = "admin"
        elif role_choice == "2":
            role = "professor"
        else:
            role = "student"

        active = True

        self.ids.append(uid)
        self.pws.append(pw)
        self.names.append(name)
        self.emails.append(email)
        self.roles.append(role)
        self.active.append(active)

        self.members.append([uid, pw, name, email, role, active])

        print("회원가입을 완료하엿습니다. ")
        print("\n[추가확인]")
        for m in self.members:
            print(m)
        print("\n[마지막 추가된 회원]")
        print(self.members[-1])

    ##########
    # 로그인
    ##########
    def login(self):
        print("\n[로그인]")
        if self.session is not None:
            print("이미 로그인 되어잇습니다. ")
            return

        uid = input("아이디: ")
        pw = input("비번: ")
        # 아이디 중복 확인
        if uid not in self.ids:
            print("아이디가 존재하지 않습니다. ")
            return
        # 현재 ID 의 인덱스 저장
        idx = self.ids.index(uid)
        # 비번 중복 확인
        if pw != self.pws[idx]:
            print("비밀번호가 틀렸습니다. ")
            return
        # 활성/비활성 확인
        if self.active[idx] is not True:
            print("비활성 계정입니다. ")
            return
        # 로그인 성공
        self.session = idx
        print(f"{self.names[idx]}({self.roles[idx]})님 로그인 성공하셨습니다!")

    ##########
    # 로그아웃
    ##########
    def logout(self):
        if self.session is None:
            print("로그인이 되어있지 않습니다. ")
            return

        self.session = None
        print("로그아웃 되었습니다. ")

    #############
    # 회원정보수정
    #############
    def member_update(self):
        if self.session is None:
            print("로그인이 되어있지 않습니다. ")
            return

        idx = self.session
        print(f"\n{self.ids[idx]}님 회원정보 수정하겠습니다. ")

        # 수정할 ID 선택
        new_id = input("아이디: ")
        # 아이디 중복 확인(현재로그인 아이디 및 기존아이디 비교)
        if new_id in self.ids:
            print("사용할 수 없는 아이디 입니다. ")
            return

        new_pw = input("비번: ")
        new_name = input("이름: ")
        new_email = input("이메일: ")

        # 기존값 유지
        new_role = self.roles[idx]
        active = self.active[idx]
        # 입력값 확인
        print(f"""
입력하신 정보는 
ID: {new_id}
PW: {new_pw}
이름: {new_name}
이메일: {new_email}
권한: {new_role}
활성화: {active} 
입니다.""")

        confirm = input("수정(Y/N): ").lower()
        # 개별리스트 수정
        if confirm == "y":
            self.ids[idx] = new_id
            self.pws[idx] = new_pw
            self.names[idx] = new_name
            self.emails[idx] = new_email
        else:
            print("회원정보가 수정되지 않았습니다. ")
            return

        # members(2차원 리스트)도 같이 수정
        self.members[idx] = [new_id, new_pw, new_name, new_email, new_role, active]
        print("회원정보가 수정되었습니다. ")
        print("\n[수정확인]")
        for m in self.members:
            print(m)

    ##########
    # 회원탈퇴
    ##########
    def member_delete(self):
        if self.session is None:
            print("로그인이 되어있지 않습니다. ")
            return
        idx = self.session
        print(f"{self.names[idx]}님 회원탈퇴하겠습니다. ")
        print("""
1. 완전탈퇴
2. 계정 비활성화
""")
        choice = input("선택: ")
        confirm = input("정말 탈퇴하시겠습니까? (Y/N): ").lower()
        if confirm != "y":
            print("회원탈퇴가 취소되었습니다. ")
            return

        # 완전탈퇴
        if choice == "1":
            self.ids.pop(idx)
            self.pws.pop(idx)
            self.names.pop(idx)
            self.emails.pop(idx)
            self.roles.pop(idx)
            self.active.pop(idx)
            self.members.pop(idx)
            print("회원님 정보가 완전히 삭제되었습니다. ")

        # 비활성화
        elif choice == "2":
            self.active[idx] = False
            self.members[idx][5] = False
            print("계정이 비활성화 되었스빈다. ")
        else:
            print("잘못된 선택입니다. ")
            return
        self.session = None
        print("회원탈퇴 완료되었습니다. ")
        # 탈퇴확인
        print("\n회원확인")
        for m in self.members:
            print(m)
