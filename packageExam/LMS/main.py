from Menu import Menu
from packageExam.LMS.common import Session
from packageExam.LMS.service import *
menu = Menu()

def main():
    MemberService.load()

    run = True
    while run:
        menu.main_menu()
        sel = input(">>>")
        if sel == "1":
            member_subrun()
        elif sel == "2":
            scores_subrun()
        elif sel == "3":
            board_subrun()
        elif sel == "4":
            item_subrun()
        elif sel == "0":
            run = False
        else:
            print("잘못입력되었습니다.")

def member_subrun():
    submenu = True
    while submenu:
        menu.member_menu()
        sel = input(">>>")
        if sel == "1":MemberService.login()
        elif sel == "2":MemberService.signup()
        elif sel == "3":MemberService.modify()
        elif sel == "4":MemberService.delete_member()
        elif sel == "9":MemberService.logout()
        elif sel == "0":return
        else:
            print("잘못입력되었습니다.")

def scores_subrun():
    submenu = True
    while submenu:
        member = Session.login_member
        ScoreService.load()
        menu.score_menu()
        sel = input(">>>")
        if sel == "1":ScoreService.list_score()
        elif sel == "2":
            if member.role == "admin":
                ScoreService.score_add()
        elif sel == "3":
            if member.role == "admin":
                ScoreService.score_modify()
        elif sel == "4":
            if member.role == "admin":
                ScoreService.score_delete()
        elif sel == "9":MemberService.logout()
        elif sel == "0":return
        else:
            print("잘못입력되었습니다.")

def board_subrun():
    submenu = True
    while submenu:
        if not Session.logout():
            print("로그인 후 이용해주세요!")
        menu.board_menu()
        sel = input(">>>")
        if sel == "1":pass
        elif sel == "2":pass
        elif sel == "3":pass
        elif sel == "4":pass
        elif sel == "9":MemberService.logout()
        elif sel == "0":return
        else:
            print("잘못입력되었습니다.")

def item_subrun():
    submenu = True
    while submenu:
        if not Session.logout():
            print("로그인 후 이용해주세요!")
        menu.item_menu()
        sel = input(">>>")
        if sel == "1":pass
        elif sel == "2":pass
        elif sel == "3":pass
        elif sel == "4":pass
        elif sel == "9":MemberService.logout()
        elif sel == "0":return
        else:
            print("잘못입력되었습니다.")



if __name__ == "__main__":
    main()