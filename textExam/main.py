from textExam.common.Session import Session
from textExam.service.MemberService import MemberService
from textExam.Menu import Menu

def main():
    MemberService.load()

    run = True
    while run:
        member = Session.login_member
        Menu.main_menu()
        select=input(">>> ")
        if select=="1":MemberService.login()
        elif select=="2":MemberService.member_add()
        elif select=="3":MemberService.modify()
        elif select=="4":MemberService.admin_member()
        elif select=="5":MemberService.logout()
        elif select=="9":MemberService.del_member()
        elif select=="0":run=False
        else:continue

if __name__=="__main__":
    main()