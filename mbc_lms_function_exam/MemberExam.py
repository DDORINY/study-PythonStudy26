# 회원관리 CRUD를 사용자 지정 함수로 만들어보자
# C : 회원가입
# R : 회원리스트 관리자인경우 회원 암호변경, 블랙리스트로 생성, 권한부여
# R : 로그인 ID와 PW를 활용하여 로그인 상태 유지 session
# U : 회원정보 수정
# D : 회원탈퇴, 회원비활성화
from wsgiref import headers
import os
# 전역 상태 변수
# run    : 프로그램 전체 종료 플래그
# subrun : 로그인 후(서브메뉴) 루프 종료 플래그
# session: 로그인 상태 저장(로그인한 회원의 인덱스, 미로그인=None)
run = True
subrun = True
session = None

FILE_NAME = "members.txt"
members = []


def save_members():
    with open(FILE_NAME,"w",encoding="utf-8") as f:
        for member in members:
            line =f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n"
            f.write(line)

def load_members():
    if not os.path.exists(FILE_NAME):
        save_members()
        return

    with open(FILE_NAME,"r",encoding="utf-8") as f:
        for line in f:
            data = line.strip().split("|")
            if data[4] == "True":
                data[4] = True
            else:
                data[4] = False

            members.append(data)
# 프로그램에서 사용될 함수들

# =========================================================
# 회원가입 (Create)
# - ID 중복 체크
# - 가입 정보 확인 후 저장
# - 저장 시 기본 권한(user), 활성 상태(True)
# =========================================================

def member_add():
    global subrun
    new_id = input("✓ ID :")
    for member in members:
        if member[0] == new_id:
            print("----------------------------------------")
            print("▶ 중복된 ID입니다.\n다른 ID를 입력해주세요.")
            return
        else:
            print(f"▶ 입력하신 ID : {new_id}")
            new_pw = input("✓ Password :")
            new_name = input("✓ Name :")

            print(f"""
    ========================================
    [회원가입 정보]
    ✓ ID : {new_id}
    ✓ Password : {new_pw}
    ✓ Name : {new_name}""")
        print("----------------------------------------")
        save = input("▶ 회원가입 하시겠습니까?\n[1] 저장\n[2] 취소\n>>>")
        if save == "1":
            print(f"▶ {new_name}님 회원가입을 환영합니다.")
            members.append([new_id, new_pw, new_name,"user",True])
            save_members()
            subrun = True
            member_login()

            if members[session][3] == "admin":
                admin_menu()

            elif members[session][3] == "user":
                user_menu()

            print("----------------------------------------")
        elif save == "2":
            print("========================================")
            print("▶ 회원가입이 취소되었습니다.")
        else:
            pass

# =========================================================
# 로그인 (Read - session 유지)
# - session이 None이면 로그인 진행
# - active=False인 계정은 로그인 불가
# - 로그인 성공 시 session에 회원 인덱스 저장
# =========================================================

def member_login():
    global session
    print("""========================================
        MBC 아카데미 회원 로그인
---------------------------------------- """)
    user_id = str(input("✓ ID :"))
    for i,member in enumerate(members):
        if not member[4] == False:
            print("----------------------------------------")
            print("▶ 비활성화/차단/회원탈퇴된 ID정보입니다.")
            return

        if member[0] ==user_id:
            user_pw = input("✓ Password :")

            if user_pw == member[1]:
                print("========================================")
                print(f"▶ {member[2]}님 안녕하세요.\n▶ 로그인되었습니다.")

                session = i


            else:
                print("▶ password가 맞지 않습니다.")
                print("----------------------------------------")
                return
        else :
            print("----------------------------------------")
            print("▶ 등록된 ID 정보가 없습니다.")

            return

# =========================================================
# 관리자 기능(Update/관리)
# - 회원 리스트 조회 후 대상 선택
# - 비밀번호 변경 / 권한 변경 / 로그인 차단 / 차단 해제
# =========================================================
def member_admin():
    global session
    if session is None:
        print("▶ 로그인 후 이용해주세요.")
        return

    elif members[session][3] == "admin" :
        member_user_list_admin()
        print("▶ 수정할 계정의 번호를 입력해주세요.")
        idx = int(input("No. >>>"))
        idx -= 1

        if idx < 0 or idx >= len(members[session]) :
            print("잘못입력되었습니다.")
            return
        else:
            select=input(f"""
========================================
 ▶ 회원의 변경하실 목록을 선택해주세요!!
========================================
 1 | 회원 암호 변경
---------------------------------------
 2 | 회원 권한 수정
---------------------------------------
 3 | 회원 로그인차단
---------------------------------------
 4 | 회원 로그인차단 해지
========================================
""")
            if select == "1":
                print("========================================")
                print(f"▶ {members[session][2]}님의 Password를 설정해주세요. ")
                user_pw =input("▶ Password :")
                sel = input(f"▶ {members[session][2]}님의 Password는 {user_pw}로 저장하시겠습니까?\n[1] 네\n[2] 아니요\n>>> ")

                if sel == "1":
                    print("------------------------------------")
                    print(f"▶ {members[session][2]}님의 Password가 변경되었습니다.")
                    members[session][1] = user_pw
                    save_members()
                elif sel == "2":
                    print("------------------------------------")
                    print(f"▶ {members[session][2]}님의 Password가 변경이 취소되었습니다.")
                    return

            elif select == "2":
                print("========================================")
                sel = input(f"▶ {members[session][2]}님의 권한을 설정해주세요\n[1] Admin\n[2] User\n>>> ")
                if sel == "1":
                    print("------------------------------------")
                    print(f"▶ {members[session][2]}님의 권한이 [Admin]으로 변경되었습니다.")
                    members[session][3] = "admin"
                    save_members()
                    return
                elif sel == "2":

                    print("------------------------------------")
                    print(f"▶ {members[session][2]}님의 권한이 [User]으로 변경되었습니다.")
                    members[session][3] = "user"
                    save_members()
                    return
                else:
                    print("▶ 잘못입력되었습니다.")
                    return

            elif select == "3":
                print("========================================")
                sel =input(f"▶ {members[session][2]}님의 로그인 차단하시겠습니까?\n[1] 네\n[2] 아니요\n>>> ")
                if sel == "1":
                    print("------------------------------------")
                    print(f"▶ {members[session][2]}님의 로그인 차단되었습니다.")
                    members[session][4] = False
                    save_members()
                    return
                elif sel == "2":
                    print("------------------------------------")
                    print(f"▶ {members[session][2]}님의 로그인 차단이 취소되었습니다.")
                    return
                else:
                    print("▶ 잘못입력되었습니다.")
                    return
            elif select == "4":
                print("========================================")
                sel = input(f"▶ {members[session][2]}님의 로그인 차단해지하시겠습니까?\n[1] 네\n[2] 아니요\n>>> ")
                if sel == "1":
                    print("------------------------------------")
                    print(f"▶ {members[session][2]}님의 로그인 차단되었습니다.")
                    members[session][4] = True
                    save_members()
                    return
                elif sel == "2":
                    print("------------------------------------")
                    print(f"▶ {members[session][2]}님의 로그인 차단해지가 취소되었습니다.")
                    return
                else:
                    print("▶ 잘못입력되었습니다.")
                    return

            else:
                print("▶ 잘못입력되었습니다.")
                return
    else:
        print("▶ Admin 권한 계정으로 로그인 후 이용해주세요!")
        return
    # 이후 처리 로직(원본 유지)
    # ...

# =========================================================
# 관리자: 회원 리스트 조회(Read)
# - admin만 조회 가능
# =========================================================
def member_user_list_admin():
    global session
    if session is None:
        print("▶ 로그인 후 이용해주세요.")
        return

    if members[session][3] != "admin" :
        print("▶ Admin 권한 계정으로 로그인 후 이용해주세요!")
        return



# =========================================================
# 로그아웃
# - session을 None으로 초기화
# =========================================================
def member_logout():
    global session
    if session is None:
        print("▶ 로그인 후 이용해주세요.")
        return
    else:
        session = None
        return



# =========================================================
# 메뉴 출력 함수들
# =========================================================
def main_menu_logout():
    print(f"""
========================================
      MBC 아카데미 회원관리 프로그램
========================================  
 1 | 회원가입   
---------------------------------------- 
 2 | 로그인  
======================================== 
 0 | 프로그램 종료
======================================== 
""")
def main_menu_login_user():
    print(f"""
========================================
      MBC 아카데미 회원관리 프로그램
========================================   
 1 | 마이페이지
---------------------------------------- 
 2 | 로그아웃
---------------------------------------- 
 3 | 회원탈퇴
======================================== 
 0 | 프로그램 종료
======================================== 
""")

def main_menu_login_admin():
    print(f"""
========================================
      MBC 아카데미 회원관리 프로그램
========================================     
 1 | 마이페이지
---------------------------------------- 
 2 | 회원리스트
---------------------------------------- 
 3 | 회원권한설정
---------------------------------------- 
 4 | 로그아웃
---------------------------------------- 
 5 | 회원탈퇴
========================================  
 0 | 프로그램 종료
======================================== 
""")

def admin_menu():
    global subrun
    while subrun:
        main_menu_login_admin()
        select = input(">>>")
        if select == "1":
            print("""========================================
      MBC 아카데미 마이페이지
---------------------------------------- """)

        elif select == "2":
            print("""========================================
      MBC 아카데미 회원리스트 
---------------------------------------- """)
            member_user_list_admin()
        elif select == "3":
            print("""========================================
      MBC 아카데미 회원권한 설정
---------------------------------------- """)
            member_admin()
        elif select == "4":
            member_logout()
            subrun = False
        elif select == "5":
            print("""========================================
      MBC 아카데미 회원탈퇴
---------------------------------------- """)

        elif select == "0":
            subrun = False
            run = False

def user_menu():
    global subrun

    while subrun:
        main_menu_login_user()
        select = input(">>>")
        if select == "1":
            print("""========================================
      MBC 아카데미 마이페이지
---------------------------------------- """)


        elif select == "2":
            member_logout()
            subrun = False
        elif select == "3":
            print("""========================================
      MBC 아카데미 회원탈퇴
---------------------------------------- """)

        elif select == "0":
            subrun = False
            run = False
# =========================================================
# 메인 루프
# - 로그아웃 상태 메뉴 → 로그인 성공 시 서브메뉴 루프 진입
# =========================================================
while run:
    main_menu_logout()
    select = input(">>>")
    if select == "1":
        print("""========================================
      MBC 아카데미 회원가입
---------------------------------------- """)
        member_add()

    elif select == "2":
        subrun = True
        member_login()

        if members[session][3] == "admin":
            admin_menu()

        elif members[session][3] == "user":
            user_menu()

    elif select == "0":
        run = False

    else:
        pass
