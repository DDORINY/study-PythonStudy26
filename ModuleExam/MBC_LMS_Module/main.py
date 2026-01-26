# 주 실행코드로 주메뉴를 담당한다.
# 외부 모듈을 호출해서 연동한다.
import MemberService # 회원관리용 클래스
import ScoreService # 학생점수관리용 클래스
import BoardService # 게시판관리용 클래스
import ItemService # 상품관리용 클래스
import Attendance # 교수전용 클래스


def main():
    run = True
    while run:
        print(f"""
    --------------------------
       MBC 아카데미 LMS 서비스
    --------------------------
    1. 회원관리
    2. 성적관리
    3. 자료 게시판
    4. 교보재관리
    5. 교수전용
    6. 취업용 게시판
    --------------------------
    0. 프로그램종료
    """)
        select = input(">>>")
        if select == "1":
            print("[회원관리 서비스]")
            # 회원관리 서비스 클래스 호출용 코드
            MemberService.MemberService().run()
            # import       class          def
        elif select == "2":
            print("[성적관리 서비스]")
            # 성적관리 서비스 클래스 호출용 코드
            ScoreService.ScoreService().run()

        elif select == "3":
            print("[자료게시판 서비스]")
            # 자료게시판 서비스 클래스 호출용 코드
            BoardService.BoardService().run()

        elif select == "4":
            print("[교보재관리 서비스]")
            # 교보재관리 서비스 클래스 호출용 코드
            ItemService.ItemService().run()

        elif select == "5":
            print("[교수전용 서비스]")
            # 교수전용 서비스 클래스 호출용 코드
            Attendance.Attendance().run()
        elif select == "6":
            print("[취업용 게시판 서비스]")
            # 취업용게시판 클래스 호출용 코드

        elif select == "0":
            print("[프로그램 종료]")
            run = False
        else:
            print("잘못입력되었습니다.")

if __name__ == "__main__":
# 여러파일을 호출하기 때문에 Main일 때만
# main()메서드를 실행
    main() # 위에서 만든 main() 함수를 실행한다.

