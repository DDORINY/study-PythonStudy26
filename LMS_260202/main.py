from LMS_260202.common.Session import Session
from LMS_260202.service import *

def main():
    MemberService.load()
    run = True
    while run:
        print("""
+--------------------------------------+
|        MBC 아카데미 LMS 프로그램       |
+--------------------------------------+
  [1] 회원가입
  [2] 로그인
  [3] 로그아웃
  [4] 회원관리
  [5] 성적관리
  [6] 게시판
  [7] 쇼핑몰
----------------------------------------
  [9] 관리자 페이지
  [0] 프로그램 종료
        """)
        select = input(">>>")
        if select == "1":MemberService.signup()
        elif select == "2":MemberService.login()
        elif select == "3":MemberService.logout()
        elif select == "4":MemberService.modify()
        elif select == "5":ScoreService.run()
        elif select == "6":BoardService.run()
        elif select == "7":pass
        elif select == "9":pass
        elif select == "0":run = False

if __name__ == "__main__":
    main()