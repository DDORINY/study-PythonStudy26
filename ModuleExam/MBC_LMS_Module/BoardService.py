import os
from datetime import datetime




class BoardService:
    def __init__(self, login_user):
        # 공지사항 리스트(2차원리스트)
        self.login_user = login_user
        self.notice_file = "notices.txt"
        self.assignment_file = "assignments.txt"
        self.practice_file = "practices.txt"
        self.anonymous_file = "anonymous.txt"
        #게시판 실행여부
        self.subrun = True



    def load_notice(self):
        notices = []

        if not os.path.exists(self.notice_file):
            open(self.notice_file, "w").close()
            return notices

        with open(self.notice_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            notices.append(line.strip())

        return notices

    def load_assignment(self):
        assignments = []

        if not os.path.exists(self.assignment_file):
            open(self.assignment_file, "w").close()
            return assignments

        with open(self.assignment_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            assignments.append(line.strip())

        return assignments

    def load_practice(self):
        practices = []

        if not os.path.exists(self.practice_file):
            open(self.practice_file, "w").close()
            return practices

        with open(self.practice_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            practices.append(line.strip())

        return practices

    def load_anonymous(self):
        anonymous = []

        if not os.path.exists(self.anonymous_file):
            open(self.anonymous_file, "w").close()
            return anonymous

        with open(self.anonymous_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            anonymous.append(line.strip())

        return anonymous









    def notice_service(self): # 1. 공지사항
        run = True
        while run:
            print("""
===========================
        [공지사항]
1. 전체 공지 목록
2. 공지 상세보기
3. 공지 작성 (admin)
0. 뒤로가기
===========================            
 """)
            select = input(">>>")

            if select == "1":
                self.notice_list()

            elif select == "2":
                self.notice_detail()

            elif select == "3":
                self.notice_write()

            elif select == "0":
                run = False

            else:
                print("잘못된 입력입니다.")
                print("다시 입력하세요.")


    # 공지사항 관련 메서드
    def notice_list(self):
        notices = self.load_notice()
        print("\n[ 전체 공지 목록 ]")

        if len(notices) == 0:
            print("등록된 공지사항이 없습니다.")
            return

        for i in range(len(notices)):
            parts = notices[i].split(" | ")

            writer = parts[1]
            content = parts[2]

            print(f"{i+1}. {content} (작성자 : {writer})")


    def notice_detail(self):
        notices = self.load_notice()

        if len(notices) == 0:
            print("공지사항이 없습니다.")
            return

        try:
            num = int(input("조회할 글 번호 >>>")) -1
        except:
            print("숫자를 입력하세요.")
            return

        if num < 0 or num >=len(notices):
            print("존재하지 않는 글 번호입니다.")
            return

        notice = notices[num]

        parts = notice.split(" | ")
        date = parts[0]
        writer = parts[1]
        content = parts[2]

        print("\n==================")
        print("[ 공지사항 상세보기 ]")
        print("--------------------")
        print(f"작성일 : {date}")
        print(f"작성자 : {writer}")
        print("--------------------")
        print(content)
        print("==================")

    def notice_write(self):
        if self.login_user[4] != "admin":
            print("관리자만 공지를 작성할 수 있습니다.")
            return

        print("\n[ 공지 작성 ]")
        content = input("공지 내용 >>> ").strip()

        if content == "":
            print("공지 내용을 입력해주세요.")
            return

        # 작성 날짜/시간
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        writer = self.login_user[0]

        notice_line = f"{now} | {writer} | {content}\n"

        with open(self.notice_file, "a", encoding="utf-8") as f:
            f.write(notice_line)

        print("공지사항이 등록되었습니다.")








    def assignment_service(self): # 2. 과제자료
        run = True
        while run:
            print("""
=============================
          [과제자료]
1. 전체 과제 목록
2. 과제 상세보기
3. 과제 등록(admin)
0. 뒤로가기
=============================
""")
            select = input(">>>")
            if select == "1":
                self.assignment_list()

            elif select == "2":
                self.assignment_detail()

            elif select == "3":
                self.assignment_write()

            elif select == "0":
                run = False

            else:
                print("잘못된 입력입니다.")
                print("다시 입력하세요.")


    def assignment_list(self):
        assignments = self.load_assignment()
        print("\n[ 전체 과제 목록 ]")

        if len(assignments) == 0:
            print("등록된 과제가 없습니다.")
            return

        for i in range(len(assignments)):
            parts = assignments[i].split(" | ")
            title = parts[2]
            writer = parts[1]
            print(f"{i+1}. {title} (작성자: {writer})")



    def assignment_detail(self):
        assignments = self.load_assignment()

        if len(assignments) == 0:
            print("등록된 과제가 없습니다.")
            return
        try:
            num = int(input("조회할 과제 번호 >>> ")) - 1
        except:
            print("숫자를 입력하세요.")
            return

        if num < 0 or num >=len(assignments):
            print("존재하지 않는 과제 번호입니다.")
            return

        assignment = assignments[num]

        parts = assignment.split(" | ")
        date = parts[0]
        writer = parts[1]
        title = parts[2]
        content = parts[3]

        print("\n==================")
        print("[    과제 상세보기   ]")
        print("--------------------")
        print(f"작성일 : {date}")
        print(f"작성자 : {writer}")
        print(f"제목 : {title}")
        print("--------------------")
        print(content)
        print("==================")

    def assignment_write(self):
        if self.login_user[4] != "admin":
            print("관리자만 과제를 등록할 수 있습니다.")
            return
        print("\n[ 과제 등록 ]")
        title = input("과제 제목 >>> ").strip()
        content = input("과제 내용 >>> ").strip()

        if title == "" or content == "":
            print("제목과 내용을 모두 입력해주세요.")
            return
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        writer = self.login_user[0]

        assignment_line = f"{now} | {writer} | {title} | {content}\n"

        with open(self.assignment_file, "a", encoding="utf-8") as f:
            f.write(assignment_line)
        print("과제가 등록되었습니다.")





    def practice_service(self): # 3. 실습자료
        run = True
        while run:
            print("""
=============================
        [실습자료]
1. 전체 실습 목록
2. 실습 상세보기
3. 실습 등록(admin)
0. 뒤로가기
=============================
""")
            select = input(">>>")
            if select == "1":
                self.practice_list()
            elif select == "2":
                self.practice_detail()
            elif select == "3":
                self.practice_write()
            elif select == "0":
                run = False
            else:
                print("잘못된 입력입니다.")
                print("다시 입력하세요.")


    def practice_list(self):
        practices = self.load_practice()
        print("\n[전체 실습 목록]")

        if len(practices) == 0:
            print("등록된 실습이 없습니다.")
            return
        for i in range(len(practices)):
            parts = practices[i].split(" | ")
            title = parts[2]
            writer = parts[1]
            print(f"{i+1}. {title} (작성자: {writer})")


    def practice_detail(self):
        practice = self.load_practice()

        if len(practice) == 0:
            print("등록된 실습이 없습니다.")
            return
        try:
            num = int(input("조회할 실습 번호 >>> ")) - 1
        except:
            print("숫자를 입력하세요.")
            return

        if num < 0 or num >=len(practice):
            print("존재하지 않는 실습 번호입니다.")
            return

        practice = practice[num]

        parts = practice.split(" | ")
        date = parts[0]
        writer = parts[1]
        title = parts[2]
        content = parts[3]

        print("\n==================")
        print("[    실습 상세보기   ]")
        print("--------------------")
        print(f"작성일 : {date}")
        print(f"작성자 : {writer}")
        print(f"제목 : {title}")
        print("--------------------")
        print(content)
        print("==================")

    def practice_write(self):
        if self.login_user[4] != "admin":
            print("관리자만 실습을 등록할 수 있습니다.")
            return
        print("\n[ 실습 등록 ]")
        title = input("실습 제목 >>> ").strip()
        content = input("실습 내용 >>> ").strip()

        if title == "" or content == "":
            print("제목과 내용을 모두 입력해주세요.")
            return
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        writer = self.login_user[0]

        practice_line = f"{now} | {writer} | {title} | {content}\n"

        with open(self.practice_file, "a", encoding="utf-8") as f:
            f.write(practice_line)
        print("실습이 등록되었습니다.")












    def anonymous_service(self): # 4. 익명질문게시판
        run = True
        while run:
            print("""
=============================
       [익명 질문 게시판]
1. 전체 글 목록
2. 글 상세보기
3. 글 작성
0. 뒤로가기
=============================
""")
            select = input(">>>")
            if select == "1":
                self.anonymous_list()
            elif select == "2":
                self.anonymous_detail()
            elif select == "3":
                self.anonymous_write()
            elif select == "0":
                run = False
            else:
                print("잘못된 입력입니다.")
                print("다시 입력하세요.")

    def anonymous_list(self):
        posts = self.load_anonymous()
        print("\n[ 전체 익명 글 목록 ]")

        if len(posts) == 0:
            print("등록된 글이 없습니다.")
            return

        for i in range(len(posts)):
            parts = posts[i].split(" | ")
            title = parts[1]
            print(f"{i+1}. {title}")

    def anonymous_detail(self):
        posts = self.load_anonymous()

        if len(posts) == 0:
            print("등록된 글이 없습니다.")
            return

        try:
            num = int(input("조회할 글 번호 >>> ")) -1
        except:
            print("숫자를 입력하세요.")
            return

        if num < 0 or num >=len(posts):
            print("존재하지 않는 글 번호입니다.")
            return

        post = posts[num]
        parts = post.split(" | ")
        date = parts[0]
        title = parts[1]
        content = parts[2]

        print("\n=================")
        print("    [글 상세보기 ]   ")
        print("-------------------")
        print(f"작성일 : {date}")
        print(f"작성자 : 익명")
        print(f"제목 : {title}")
        print(content)
        print("==================")


    def anonymous_write(self):
        print("\n[ 글 작성 ]")
        title = input("글 제목 >>> ").strip()
        content = input("글 내용 >>> ").strip()

        if title == "" or content == "":
            print("제목과 내용을 모두 입력해주세요.")
            return

        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        post_line = f"{now} | {title} | {content}\n"

        with open(self.anonymous_file, "a", encoding="utf-8") as f:
            f.write(post_line)

        print("글이 등록되었습니다.")





    def free_service(self): # 5. 자유게시판
        pass













































    def run(self):
        subrun = True
        while subrun:
            print("""
================================
1. 공지사항(admin)
2. 과제자료(admin)
3. 실습자료(admin)
4. 익명질문게시판
5. 자유게시판
9. 자료게시판서비스종료
================================
""")
            select = input(">>>")
            if select == "1":
                print(" 공지사항 ")
                self.notice_service()

            elif select == "2":
                print(" 과제자료 ")
                self.assignment_service()

            elif select == "3":
                print(" 실습자료 ")
                self.practice_service()

            elif select == "4":
                print(" 익명질문게시판 ")
                self.anonymous_service()

            elif select == "5":
                print(" 자유게시판 ")

            elif select == "9":
                print(" 자료게시판서비스종료 ")
                subrun = False
            else:
                print("잘못된입력입니다.")






if __name__ == "__main__":
    # 테스트용 로그인 유저 (관리자)
    login_user = ["admin", "1234", "관리자", "email", "admin"]

    board = BoardService(login_user)
    board.run()

