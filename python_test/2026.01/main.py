# 대부분 프로그래밍에서 1번이 되는 (start) 파일을 main으로 만든다.


# MBC 아카데미 LMS 프로그램을 만들어보자.
# 회원관리 : 회원가입/로그인 -> 회원구분 | 시스템담당자, 교수, 행정, 학생, 손님, 학부모
# 성적관리 |
# 교수- > 성적등록,수정|수강과목 신청 |과제
# 행정 -> 1년에 1번 또는 학기마다 백업(이전->삭제)
# 학생 -> 개인성적일람, 성적출력
# 손님 -> 학교소개페이지 열람
# 학부모 -> 자녀학사관리
# 게시판 | 회원제, 비회원제, 문의사항, Q/A

# 필요한 변수
run = True # 메인 메뉴용 while
subrun = True # 보조 메뉴용 while
session = None # 로그인한 사용자의 인덱스를 기억

# [필요한 리스트]
# 회원에 대한 리스트
sns = [1,2] # 회원에 대한 번호
ids = ["kkw","kdh"] # 로그인 아이디
pws = ["1234","1234"] # 암호에 대한 리스트
group = ["admin","stu"] # 회원등급 |admin:관리자|stu:학생|guest :비회원 |teacher :선생
# 회원가입에 대한 리스트
names = ["김기원","김도하"] # 이름
numbers =["010-1234-1234","010-2345-6789"] # 연락처
ssn = ["160604-1234567","170705-2345678"] # 주민번호
moneys = ["1,000,000","1,000,000"]

# 성적에 대한 리스트
pythonScore = [0,0] # 파이썬 점수들
dataBaseScore = [0,0] # 데이터베이스 점수들
wwwScore = [0,0] # 프론트 점수들
totalScore = [0,0] # 총점들
avgScore = [0,0] # 평균 들
gradeScore =["A","A"] # 등급 들
stuIdx = [] # 학생들의 인덱스 (학번)<=> 회원은 sns

# 게시판에 대한 리스트
board_no = [] # 게시물의 번호
board_title = [] # 게시물 제목
board_content = [] #게시물의 내용
board_writer = [] # 게시물 작성자 <-> 회원의 sns
board_password = [] #게시물의 암호 <-> 비회원인 경우
board_Announcement = [] # 공지게시물
board_bulletin1 =[] #공지게시판과 강의 게시판 구분 //강의실 공지 =1|MBC아카데미 소식 게시판=2

#메뉴구형
mainMenu = """———————————————————————————————
MBC 아카데미 LMS에 오신걸 환영합니다.
———————————————————————————————
[1] 로그인|회원가입
[2] 성적관리
[3] MBC 아카데미 소식
[4] 관리자 메뉴
[5] 등록금 입금 안내|입금
[6] 프로그램 종료"""

memberMenu = """———————————————————————————————
[회원관리 메뉴]
[1] 로그인
[2] 회원가입
[3] 회원수정
[4] 돌아가기
[5] 로그아웃
[6] 회원탈퇴"""

scoreMenu1 = """———————————————————————————————
[성적관리 메뉴]
[1] 성적입력
[2] 성적전체보기
[3] 성적수정
[4] 성적백업
[5] 돌아가기
[6] 로그아웃""" #교수 및 행정관리자용

scoreMenu2 = """———————————————————————————————
[성적관리 메뉴]
[1] 강의소개
[2] 성적조회
[3] 강의게시판
[4] 돌아가기
[5] 로그아웃""" #학생용

boardMenu1 = """———————————————————————————————
[회원제 게시판]
[1] 공지사항
[2] 새글작성
[3] 게시판리스트
[4] 게시글 수정|삭제
[5] 돌아가기
[6] 로그아웃"""

adminMenu ="""———————————————————————————————
[1] 학생조회 | 전체리스트
[2] 공지등록 | 비회원게시판관리
[3] 등록금입금등록
[4] 등록금입금내역
[5] 권한부여설정
[6] 돌아가기
[7] 로그아웃"""

#주 실행문 구현

while run:
    print(mainMenu) #메인메뉴 호출용
    select = input(">>>")

    if select == "1":
        subrun = True
        while subrun: #부메뉴 반복용
            print(memberMenu) #로그인 또는 회원가입 메뉴 호출용
            subselect = input(">>>") # 회원부메뉴 선택값을 넣음
            if subselect == "1":
                print("———————————————————————————————")
                print("[아이디와 비밀번호를 입력]") #로그인
                id = input("아이디|").strip()
                if id in ids:
                    idx = ids.index(id)
                    if group[idx] == "out":
                        print("회원탈퇴 아이디입니다.")
                        continue

                    pw = input("비밀번호|").strip()
                    if pw == pws[idx]:
                        print("로그인되었습니다.")
                        session = idx
                    else:
                        print("비밀번호가 맞지 않습니다.")
                else:
                    print("아이디정보가 존재하지 않습니다.")


            elif subselect == "2":
                print("———————————————————————————————")
                print("[회원가입 메뉴]")  # 회원가입
                name = input("이름| ").strip()
                sn = input("주민번호| ").strip()
                number = input("연락처| ").strip()
                id = input("아이디| ").strip()
                pw = input("비밀번호| ").strip()
                print("———————————————————————————————")
                print(f"이름:{name}|주민번호:{sn}|연락처:{number}|아이디:{id}|비밀번호:{pw}\n입력해주신 정보가 맞으신가요?(y/n)")
                sel=input(">>>").strip()
                if sel == "y":
                    print(f"학번은 {len(sns)+1} 회원가입이 완료되었습니다.\n감사합니다.")

                    print("▶ 등록금 입금 시 권한이 자동으로 생성됩니다.")

                    #회원의 정보
                    names.append(name)
                    ssn.append(sn)
                    numbers.append(number)
                    ids.append(id)
                    pws.append(pw)
                    group.append("guest")

                    #학생고유번호
                    no = len(sns)+1
                    sns.append(no)

                    # 입금 여부
                    moneys.append("0")

                    #학생의성적처리 =인덱스의 값은 0이며 숫자형 데이터이다.
                    python = 0
                    dataBase = 0
                    www =0

                    total =python+dataBase+www
                    avg =total/3

                    if avg >= 90:
                        grade="A"
                    elif avg >= 80:
                        grade="B"
                    elif avg >= 70:
                        grade="C"
                    elif avg >= 60:
                        grade="D"
                    else:
                        grade="F"

                    pythonScore.append(python)
                    dataBaseScore.append(dataBase)
                    wwwScore.append(www)
                    totalScore.append(total)
                    avgScore.append(avg)
                    gradeScore.append(grade)
                elif sel == "n":
                    print("회원가입이 취소되었습니다.")
                else:
                    pass



            elif subselect == "3":
                if session is None:
                    print("로그인 후 이용해주세요!")
                    continue

                if group[session]:
                    print("———————————————————————————————")
                    print("[내 정보 수정]")  # 내정보 수정
                    print(f"{sns[session]}학번. {names[session]}님 안녕하세요.\n {names[session]}의 정보를 수정해주세요.")
                    print("———————————————————————————————")
                    names[session] = input(f"이름 : {names[session]} |")
                    numbers[session] = input(f"연락처 : {numbers[session]} |")
                    print(f"수정이 완료되었습니다.\n [수정된 정보] \n이름 : {names[session]}|연락처 : {numbers[session]}")



            elif subselect == "4": #돌아가기
                subrun = False

            elif subselect == "5":
                print("———————————————————————————————")
                print("[로그아웃]")  # 로그아웃
                session = None
                subrun = False

            elif subselect == "6":
                print("———————————————————————————————")
                print("[회원탈퇴]")  # 회원탈퇴
                if session is None:
                    print("로그인 후 이용해주세요.")
                    continue
                if group[session]:
                    sel2 =input(f"{names[session]}님 회원탈퇴를 진행하시겠습니까? (y/n) \n>>>")
                    if sel2 == "y":
                        print("회원탈퇴가 진행되었습니다. \n이용해주셔서 감사합니다.\n 회원정보는 6개월간 보존되며 이후 삭제됩니다.")
                        group[session] = "out"


                    elif sel2 == "n":
                        print("회원탈퇴가 취소되었습니다.")
                    else:
                        print("잘못 입력되었습니다.")
            else:
                pass
    elif select == "2":
        if session is None:
            print("로그인 후 이용해주세요!")
            continue

        subrun = True
        while subrun:
            if group[session] in ("teacher","admin"): #선생님/관리자 성적관리메뉴
                print(scoreMenu1)
                sel1=input(">>>").strip()
                if sel1 == "1":
                    print("———————————————————————————————")
                    print(f"{names[session]} 선생님.\n안녕하세요!\n성적입력페이지입니다.") #성적입력
                    sn = int(input("학번 |"))
                    if sn in sns:
                        stuIdx = sns.index(sn)
                        stu_sel=input(f"{names[stuIdx]} 학생의 성적을 입력하시겠습니까?(y/n)")
                        if stu_sel == "y":
                            python = int(input("파이썬 점수 | "))
                            dataBase = int(input("데이터베이스 점수 | "))
                            www = int(input("프론트 점수 | "))

                            total =python+dataBase+www
                            avg = total / 3

                            if avg >= 90:
                                grade = "A"
                            elif avg >= 80:
                                grade = "B"
                            elif avg >= 70:
                                grade = "C"
                            elif avg >= 60:
                                grade = "D"
                            else:
                                grade = "F"

                            print("[입력하신 점수를 확인하시고 맞으신가요?(y/n)")
                            print(f"파이썬 점수 : {python}|데이터베이스 점수 : {dataBase}|프론트 점수:{www}")
                            print(f"총점 :{total}|평균 :{avg}|등급 :{grade}")
                            sel3 = input(">>>").strip()

                            if sel3 == "y":
                                print(f"{names[stuIdx]}성적등록이 완료되었습니다.")
                                pythonScore[stuIdx]=python
                                dataBaseScore[stuIdx]=dataBase
                                wwwScore[stuIdx]=www
                                totalScore[stuIdx]=total
                                avgScore[stuIdx]=avg
                                gradeScore[stuIdx]=grade

                            elif sel3 == "n":
                                print("성적입력이 취소되었습니다.")

                        elif stu_sel == "n":
                            print("성적입력이 취소되었습니다.")


                    else:
                         print("등록된 학번이 없습니다. ")


                elif sel1 == "2":

                    print("———————————————————————————————")
                    print(f"{names[session]} 선생님.\n안녕하세요!\n성적리스트 페이지입니다.")  # 성적리스트
                    #학생 성적 전체리스트
                    for i in range(len(group)):
                        if group[i] == "stu":
                            print(f"{i}. {sns[i]}학번| {names[i]}\n파이썬| {pythonScore[i]}점 ,데이터베이스| {dataBaseScore[i]}점, 프론트| {wwwScore[i]}점\n총점| {totalScore[i]}점,평균| {avgScore[i]},등급| {gradeScore[i]}\n____________________ ")
                    no = int(input("학생성적조회를 원하시는 경우\n학번을 검색해주세요!>>>"))
                    if no in sns:
                        stuIdx = sns.index(no)
                        print(f"{sns[stuIdx]}학번| {names[stuIdx]}\n파이썬| {pythonScore[stuIdx]}점 ,데이터베이스| {dataBaseScore[stuIdx]}점, 프론트| {wwwScore[stuIdx]}점\n총점| {totalScore[stuIdx]}점,평균| {avgScore[stuIdx]},등급| {gradeScore[stuIdx]}\n____________________")
                    else:
                        print("등록된 학번이 없습니다. ")

                elif sel1 == "3":
                    print("———————————————————————————————")
                    print(f"{names[session]} 선생님.\n안녕하세요!\n성적수정 페이지입니다.")  # 성적수정

                    no = int(input("수정하실 학생의 학번을 검색해주세요!>>>"))

                    if no in sns:
                        stuIdx = sns.index(no)
                        print(f"{names[stuIdx]}학생의 성적을 수정합니다.")
                        python = int(input(f"파이썬 (현재점수 {pythonScore[stuIdx]}) | "))
                        dataBase = int(input(f"데이터베이스 (현재 점수 {dataBaseScore[stuIdx]}) | "))
                        www = int(input(f"프론트 (현재점수 {wwwScore[stuIdx]}) | "))

                        total = python + dataBase + www
                        avg = total / 3

                        if avg >= 90:
                            grade = "A"
                        elif avg >= 80:
                            grade = "B"
                        elif avg >= 70:
                            grade = "C"
                        elif avg >= 60:
                            grade = "D"
                        else:
                            grade = "F"

                        print("[입력하신 점수를 확인하시고 맞으신가요?(y/n)")
                        print(f"파이썬 점수 : {python}|데이터베이스 점수 : {dataBase}|프론트 점수:{www}")
                        print(f"총점 :{total}|평균 :{avg}|등급 :{grade}")
                        sel5 = input(">>>").strip()
                        if sel5 == "y":
                            print(f"{names[stuIdx]}성적등록이 완료되었습니다.")
                            pythonScore[stuIdx] = python
                            dataBaseScore[stuIdx] = dataBase
                            wwwScore[stuIdx] = www
                            totalScore[stuIdx] = total
                            avgScore[stuIdx] = avg
                            gradeScore[stuIdx] = grade
                        elif sel5 == "n":
                            print("성적수정이 취소되었습니다.")
                        else:
                            print("잘못입력되었습니다.")
                    else:
                        print("등록된 학번이 없습니다.")

                elif sel1 == "4":
                    print("———————————————————————————————")
                    print(f"{names[session]} 선생님.\n안녕하세요!\n성적백업 페이지입니다.")  # 성적백업
                    b_up = input("전체 학생리스트를 백업하시겠습니까?(y/n)")
                    print("정상적으로 백업처리가 완료되었습니다.")

                elif sel1 == "5":
                    subrun = False

                else:
                    print("———————————————————————————————")
                    print("[로그아웃]")  # 로그아웃
                    session = None
                    subrun = False




            elif group[session] == "stu": #학생 성적관리메뉴
                print(scoreMenu2)
                sel1 = input(">>>").strip()
                if sel1 == "1":
                    print("———————————————————————————————")
                    print("[강의소개]")  # 비회원용 게시판
                    print("""

파이썬으로 로직을 만들고, 데이터베이스로 정보를 관리하며, 프론트엔드로 화면을 구현하는
실무 중심 IT 교육 과정입니다.

파이썬 (Python)
———————————————————————————————
파이썬은 문법이 쉽고 활용 범위가 넓어 프로그래밍 입문자에게 가장 적합한 언어입니다.
웹 서비스 개발, 데이터 분석, 인공지능(AI), 자동화 프로그램 등 다양한 분야에서 사용되며, 
실제 산업 현장에서 가장 많이 활용되는 언어 중 하나입니다.
본 과정에서는 파이썬을 통해 기초 코딩 능력과 문제 해결 능력을 단계적으로 학습합니다.

데이터베이스 (Database)
———————————————————————————————
데이터베이스는 정보를 체계적으로 저장하고 관리하는 기술입니다.
회원 정보, 성적 관리, 주문 내역 등 대부분의 서비스는 데이터베이스를 기반으로 운영됩니다.
본 과정에서는 SQL을 활용하여 데이터를 조회·추가·수정·삭제하는 방법을 배우며,
실무에서 바로 활용 가능한 데이터 관리 및 분석 기초 역량을 기를 수 있습니다

프론트엔드 (Frontend)
———————————————————————————————
프론트엔드는 사용자가 직접 보고 사용하는 웹 화면을 만드는 기술입니다.
HTML, CSS, JavaScript를 활용하여 웹 페이지의 구조, 디자인, 동작을 구현합니다.
본 과정에서는 홈페이지와 웹 서비스의 기본 화면을 직접 제작해 보며,
사용자 경험(UI/UX)을 고려한 웹 구현 능력을 키우는 것을 목표로 합니다.
                    """)
                elif sel1 == "2":
                    print("———————————————————————————————")
                    print("[성적조회]")  # 비회원용 게시판
                    print(f"""{names[session]}님. 반갑습니다.
파이썬 (Python)       |{pythonScore[session]}
데이터베이스 (Database)|{dataBaseScore[session]}
프론트엔드 (Frontend)  |{wwwScore[session]}
총점 | {totalScore[session]}\t 평균 | {avgScore[session]}\t 등급 | {gradeScore[session]}""")


                elif sel1 == "3":
                    print("———————————————————————————————")
                    print("[강의게시판]")  # 비회원용 게시판
                    for i in range(len(board_no)):
                        if board_Announcement[i] == "Y" and board_bulletin1[i] == "1" :
                            print(f"""
[공지]{board_title[i]} {board_writer[i]}""")
                        if board_Announcement[i] == "N" and board_bulletin1[i] == "1" :
                            print(f"""
{i}.{board_title[i]} {board_writer[i]}""")

                    new = input("게시글 작성 (y/n) \n>>>")
                    if new == "y":
                        title = input("제목 |").strip()
                        content = input("내용 |").strip()
                        writer = names[session]
                        passwords = pws[session]
                        print("———————————————————————————————")
                        sel2 = input("저장하시겠습니까? (y/n)").strip()
                        if sel2 == "y":
                            print("게시글로 정상적으로 등록이 완료되었습니다.")

                            no = len(board_no) + 1
                            board_no.append(no)
                            board_title.append(title)
                            board_content.append(content)
                            board_writer.append(writer)
                            board_password.append(passwords)
                            board_Announcement.append("N")
                            board_bulletin1.append("1")


                    elif new == "n":
                        print("게시글 작성이 취소되었습니다.")
                    else:
                        print("잘못 입력되었습니다.")

                    no = int(input("게시글 번호를 입력해주시면 자세히 보실 수 있습니다.\n>>>"))
                    if no in board_no:
                        no_idx = board_no.index(no)
                        print(f"""
                    제목 :{board_title[no_idx]} 
                    내용 :{board_content[no_idx]} 
                    작성자 :{board_writer[no_idx]}""")
                        board_1 = input("[1]수정 [2] 삭제 >>>")
                        if board_1 == "1":
                            print("게시글을 수정해주세요")
                            pw = input("암호 :")
                            if pw in board_password:
                                idx = board_password.index(pw)
                                board_title[no_idx] = input("제목 :")
                                board_content[no_idx] = input("내용 :")
                                print("게시물이 수정되었습니다.")

                        elif board_1 == "2":
                            pw = input("암호 :")
                            if pw in board_password:
                                idx = board_password.index(pw)

                                board_no.pop(idx)
                                board_title.pop(idx)
                                board_content.pop(idx)
                                board_writer.pop(idx)
                                board_password.pop(idx)
                                board_Announcement.pop(idx)
                                board_bulletin1.pop(idx)


                elif sel1 == "4":
                    subrun = False

                elif sel1 == "5":
                    print("———————————————————————————————")
                    print("[로그아웃]")  # 로그아웃
                    session = None
                    subrun = False
                else:
                    pass
            else:
                print("서비스 이용 권한이 없습니다. 관리자에게 문의해주세요!")
                subrun = False
    elif select == "3":
        print("———————————————————————————————")
        print("[MBC 아카데미 소식]")  # 비회원용 게시판
        for i in range(len(board_no)):
            if board_Announcement[i] == "Y" and board_bulletin1[i] == "0":
                print(f"""[공지]{board_title} {board_writer[i]}""")
            if board_Announcement[i] == "N" and board_bulletin1[i] == "0":
                print(f"""{i}.{board_title} {board_writer[i]}""")

        new = input("게시글 작성 (y/n) \n>>>")
        if new == "y":
            title = input("제목 |").strip()
            content = input("내용 |").strip()
            writer = input("작성자 |").strip()
            passwords = input("암호 |").strip()
            print("———————————————————————————————")
            sel2 = input("저장하시겠습니까? (y/n)").strip()
            if sel2 == "y":
                print("게시글로 정상적으로 등록이 완료되었습니다.")

                no = len(board_no) + 1
                board_no.append(no)
                board_title.append(title)
                board_content.append(content)
                board_writer.append(writer)
                board_password.append(passwords)
                board_Announcement.append("N")
                board_bulletin1.append("0")
            elif sel2 == "n":
                print("게시글이 취소되었습니다.")
        elif new == "n":
            no =input("게시글 번호를 입력해주시면 자세히 보실 수 있습니다.\n>>>")
            if no in board_no:
                no_idx = board_no.index(no)
                print(f"""
제목 :{board_title[no_idx]} 
내용 :{board_content[no_idx]} 
작성자 :{board_writer[no_idx]}""")
                board_1= input("[1]수정 [2] 삭제 >>>")
                if board_1 == "1":
                    print("게시글을 수정해주세요")
                    pw = input("암호 :")
                    if pw in board_password:
                        idx = board_password.index(pw)
                        board_title[no_idx] =input("제목 :")
                        board_content[no_idx]=input("내용 :")
                        print("게시물이 수정되었습니다.")

                elif board_1 == "2":
                    pw =input("암호 :")
                    if pw in board_password:
                        idx = board_password.index(pw)

                        board_no.pop(idx)
                        board_title.pop(idx)
                        board_content.pop(idx)
                        board_writer.pop(idx)
                        board_password.pop(idx)
                        board_Announcement.pop(idx)
                        board_bulletin1.pop(idx)

            else:
                print("없는 게시글 번호입니다.")


    elif select == "4":
        if session is None:
            print("관리자 전용 페이지 입니다. 로그인 후 이용해주세요!")
            continue
        if group[session] == "admin":
            print("———————————————————————————————")
            print(adminMenu)  #관리자 메뉴
            select = input(">>>").strip()
            if select == "1":
                print("———————————————————————————————")
                print("[학생조회]")  # 현재 등록된 전체 학생리스트 조회
                for i in range(len(sns)):
                    if group[i] == "stu":
                        print(f"{sns[i]}학번. {names[i]} 연락처 :{numbers[i]}|현재수업 진행 중")
                    elif group[i] == "out":
                        print(f"{sns[i]}학번. {names[i]} 연락처 :{numbers[i]}|탈퇴 회원")
                    elif group[i] == "guest":
                        print(f"{sns[i]}학번. {names[i]} 연락처 :{numbers[i]}|수업 미신청 회원|등록금 미입금")
                    else:
                        pass

            elif select == "2":
                print("———————————————————————————————")
                print("[공지글 생성 페이지]")  # 공지등록&강의게시판 관리 및 MBC아카데미 소식 게시판
                bo_sel=input("등록할 게시판을 선택해주세요. \n(강의실 공지 =y|MBC아카데미 소식 게시판=n)\n>>>")
                if bo_sel == "y":
                    title = input("제목 |").strip()
                    content = input("내용 |").strip()
                    writer = names[session]
                    passwords = pws[session]
                    print("———————————————————————————————")
                    sel2 = input("저장하시겠습니까? (y/n)").strip()
                    if sel2 == "y":
                        print("공지글로 정상적으로 등록이 완료되었습니다.")

                        no = len(board_no) + 1
                        board_no.append(no)
                        board_title.append(title)
                        board_content.append(content)
                        board_writer.append(writer)
                        board_password.append(passwords)
                        board_Announcement.append("Y")
                        board_bulletin1.append("1")
                elif bo_sel == "n":
                    title = input("제목 |").strip()
                    content = input("내용 |").strip()
                    writer = names[session]
                    passwords = pws[session]
                    print("———————————————————————————————")

                    sel2 = input("저장하시겠습니까? (y/n)").strip()
                    if sel2 == "y":
                        print("공지글로 정상적으로 등록이 완료되었습니다.")
                        no = len(board_no) + 1
                        board_no.append(no)
                        board_title.append(title)
                        board_content.append(content)
                        board_writer.append(writer)
                        board_password.append(passwords)
                        board_Announcement.append("Y")
                        board_bulletin1.append("0")





            elif select == "3":
                print("———————————————————————————————")
                print("[등록금입금등록]")  # 등록금입금등록
                print("현금 결제한 학생들의 등록금 입금 등록페이지 입니다.")
                no = int(input("등록된 학생의 학번을 입력해주세요.\n>>>"))
                if no in sns:
                    stuIdx = sns.index(no)
                    print(f"{names[stuIdx]}의 등록금을 입금하시겠습니까?")
                    money = input("입금처리하실 금액을 입력해주세요!\n>>>").strip()
                    sel2 =input(f"입금 금액은 {money}입니다. (y/n)")
                    if sel2 == "y":
                        print("등록금 입금등록이 완료되었습니다.")
                        moneys[stuIdx]= money
                        group[stuIdx] = "stu"
            elif select == "4":
                print("———————————————————————————————")
                print("[등록금입금내역]") #등록금입금내역
                print("전체 입금 내역입니다.")
                for i in range(len(sns)):
                    if group[i] == "stu":
                        print(f"{sns[i]}학번의 {names[i]}님 | {moneys[i]}원 현금입금")
            elif select == "5":
                print("———————————————————————————————")
                print("[권한부여설정]")
                no = int(input("강제 권한 설정 페이지 입니다.\n변경하실 고유학번 번호를 입력해주세요\n>>>"))

                if no in sns:
                    idx = sns.index(no)
                    sel2=input(f"{names[idx]}님의 권한일 변경하시겠습니까?\n현재 권한은 {group[idx]}입니다.\n 번경하실 번호를 입력해주세요.\n [1] 학생 [2] 선생님 [3] 게스트 [4] 관리자 [5] 강제탈퇴")
                    if sel2 == "1":
                        print("권한이 학생으로 변경되었습니다.")
                        group[idx]="stu"
                    elif sel2 == "2":
                        print("권한이 선생님으로 변경되었습니다.")
                        group[idx]="teacher"
                    elif sel2 == "3":
                        print("권한이 게스트으로 변경되었습니다.")
                        group[idx] = "guest"
                    elif sel2 == "4":
                        print("권한이 관리자으로 변경되었습니다.")
                        group[idx] = "admin"
                    elif sel2 == "5":
                        print("권한이 강제탈퇴되었습니다..")
                        group[idx] = "out"
                    else:
                        print("잘못 입력되었습니다.")
                else:
                    print("등록된 학번이 없습니다.")

            elif select == "6": #돌아가기
                subrun = False
            elif select == "7":# 로그아웃
                print("———————————————————————————————")
                print("[로그아웃]")
                session = None
                subrun = False


        else:
            print("관리자 아이디가 아닙니다.")
            continue
    elif select == "5":
        print("———————————————————————————————")
        print("[등록금 안내]")
        no = int(input(f"등록금을 입금하실 학생의 학번을 입력해주세요.\n>>>"))
        if no in sns:
            stuIdx = sns.index(no)
            stu_mo =input(f"{names[stuIdx]}님 안녕하세요.\n등록금 금액 : 1,000,000원\n입금하시겠습니까? (y/n)")
            if stu_mo == "y":
                print("입금처리가 완료되었습니다.")
                moneys[stuIdx]="1,000,000"
                group[stuIdx]="stu"
            else:
                print("등록금 입금이 취소되었습니다.")
        else:
            print("등록되지 않은 학번입니다.\n 회원가입 후 다시 진행해주세요.")

    elif select == "6":
        print("———————————————————————————————")
        print("MBC 아카데미 LMS 프로그램이 종료됩니다.\n 이용해주셔서 감사합니다.")
