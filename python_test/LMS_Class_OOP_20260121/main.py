from Menu import Menu
from MemberService import MemberService


def main():
    run = True
    menu = Menu()
    members = MemberService()

    while run:
        menu.main_menu()  # 메인메뉴
        sel = input(">>> ")  # 입력
        if sel == "1":
            members.members_add()  # 회원가입
        elif sel == "2":
            members.members_login()
            members.subrun(menu)# 로그인
        elif sel == "3":
            pass  # 공지사항
        elif sel == "4":
            pass  # 자유게시판 (읽기전용)
        elif sel == "0":
            run = False  # 프로그램 종료
        else:
            print("입력오류")



if __name__ == "__main__":
    main()
