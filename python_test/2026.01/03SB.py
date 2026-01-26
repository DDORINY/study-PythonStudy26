import time
# 목표 : MBC 아카데미 LMS 프로그램을 만들어 보자.
# 회원관리 : 시스템담당자, 교수, 행정(1년에 한 번씩 백업 이전하면서 삭제), 학생, 손님, 학부모
# 성적관리 : 교수가 성적등록, 수정,
# 학생 : 개인성적 일람 + 비회원 게시판 + 성적 출력
# 손님 : 학교 소개페이지 열람
# 학부모 : 자녀학사관리 등등
# 게시판 : 회원제, 비회원제, 문의사항, QNA

# 필요한 변수
run = True # 메인 메뉴용
session = None # 로그인한 사용자의 인덱스를 기억   (세션은 서버에서 가지고 있다가 회신해 주는 것, 쿠키는 내 컴퓨터에서 기억하고 있는 것)

# 필요한 리스트
# 회원에 대한 리스트
sns = ["1"] # 회원에 대한 번호
ids = ["kkw"] #id에 대한 리스트
names = ["김기원"]
passwords = ["1234"] #pw에 대한 리스트
emails = ["kkw@mbc.com"]
group = ["Admin"] # 회원등급
#admin (관리자), stu(학생), ofc(행정), guest(손님)     if admin(idx) == "stu" or "admin":  이런 식으로 작성

# 성적에 대한 리스트
pythonScore = [0] #파이썬점수들
dataBaseScore = [0] #데이터베이스 점수들
wwwScore = [0] #프론트 점수들
totalScore = [0] # 총점
avgScore = [0] # 평균
gradeScore = [0] # 등급 들
stuNum = ["320-01"] # 학생의 인덱스 (학번) - 회원의 sns와 연결
stuName = []
# 게시판에 대한 리스트
board_no = []
board_title = []
board_score = []
board_writer = [] # 게시물 작성자 회원의 sns와 연결

# 메뉴 구성
mainMenu = """
================================
MBC 아카데미 LMS에 오신걸 환영합니다.
[메인 메뉴입니다.]
1. 로그인(회원가입)
2. 성적관리
3. 게시판
4. 관리자메뉴
9. 프로그램 종료
================================
"""
memberMenu = """
------[회원관리 메뉴입니다.]------
1. 로그인
2. 회원가입
3. 회원수정
4. 회원탈퇴
9. 메인 메뉴로 이동
"""
scoreMenu = """
------[성적관리 메뉴입니다.]------
1. 성적입력(교수전용)
2. 성적보기(개인용)
3. 성적수정(교수전용)
4. 성적백업(행정직원전용)
9. 메인 메뉴로 이동
"""
boardMenu = """
------[회원제 게시판 입니다.]------
1.
2.
3.
4.
9. 메인 메뉴로 이동
"""
adminMenu = """
------[관리자 메뉴 입니다.]------
1. 회원 전체 보기
2. 
3.
4.
9. 메인 메뉴로 이동
"""
# 주 실행문
while run:
    print(mainMenu)
    if session is not None:
        if group[session] == "Admin":
            print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[관리자 권한]")
        elif group[session] == "Professor":
            print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[교수 권한]")
        elif group[session] == "Student":
            print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[학생 권한]")
        else:
            print("외부 사용자 입니다.")
    select = input("이용하시려는 메뉴 번호를 선택하세요.") # 사용자가 주메뉴선택 값을 select 넣는다.
##############################################################################################################
    if select == "1":
        print("\n로그인(회원가입)메뉴로 진입합니다.")
        subRun = True
        while subRun == True:
            print(mainMenu)
            if session is not None:  #메인메뉴나 서브메뉴 진입시에 계속 사용자의 권한과 로그인 상태를 확인시켜서 꼬이는 게 있는지 확인하는 방법
                if group[session] == "Admin":
                    print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[관리자 권한]")
                elif group[session] == "Professor":
                    print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[교수 권한]")
                elif group[session] == "Student":
                    print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[학생 권한]")
                else:
                    print("외부 사용자 입니다.")
            print(memberMenu)
            subSelect = input("이용하시려는 회원메뉴 번호를 선택하세요.")
#------------------------------------------------------------------------------------------------------------
            # 1-1 로그인 메뉴
            if subSelect == "1":
                print("\n로그인 메뉴로 진입합니다.")
                while True:
                    id = input("아이디를 입력하세요 :")
                    if id in ids:
                        idx = ids.index(id)
                        while True:
                            pw = input("패스워드를 입력하세요 :")
                            if passwords[idx] == pw:
                                session = idx
                                print(f"\n{names[idx]}님 로그인 성공\n메인화면으로 이동합니다.")
                                time.sleep(1)
                                subRun = False
                                break
                            else:
                                print("\n입력한 패스워드가 맞지 않습니다.\n다시 입력하세요.")
                    else:
                        print("\n입력한 ID는 회원가입 되어있지 않습니다.\n회원 관리 메뉴로 이동합니다.")
                        time.sleep(1)
                    break
# ------------------------------------------------------------------------------------------------------------
            # 1-2 회원가입 메뉴
            elif subSelect == "2":
                print("\n[회원가입 메뉴입니다.]")
                while True:
                    id = input("아이디 : ")
                    if id in ids:
                        print("\n이미 존재하는 아이디입니다.\n회원 메뉴로 돌아갑니다.")
                        time.sleep(1)
                        break
                    else:
                        pw = input("비밀번호 : ")
                        name = input("이름 : ")
                        email = input("이메일 : ")
                        print(f"\n입력하신 정보를 확인하세요\n이름 : {name} | 아이디 : {id} | 이메일 : {email}")
                        if input("가입하시겠습니까? (y/n)").lower() == "y":
                            if not stuNum:
                                st = "320-01"    #처음 생성되는 계정이면 무조건 번호를 320-01로 만들게 하고
                            else:
                                last_sn = stuNum[-1]                         #처음 생성되는 계정이 아니면 마지막 생성된 stuNum을 가져와서
                                last_num = int(last_sn.split("-")[1])        #- 표를 기준으로 문자를 나누고 - 뒷쪽에 있는 문자를 정수로 바궈서 가져오되
                                new_num = last_num + 1                       #가져온 점수 +1을 뉴넘에 넣어두고
                                st = (f"320-{new_num:02d}")  # 뉴 넘버를 뒤와같이 표현한다 f"(1:02d)" 정수 표현식 전체 두 자리를 만들되 부족한 부분은 0으로 채우고 정수로 해라
                            stuNum.append(st)
                            new_sns = int(sns[-1]) + 1   #인덱싱이 0부터 시작이니 회원의 순서는 +1 되어야 한다.
                            sns.append(str(new_sns))
                            ids.append(id)
                            passwords.append(pw)
                            names.append(name)
                            emails.append(email)
                            pythonScore.append(0)
                            dataBaseScore.append(0)
                            wwwScore.append(0)
                            totalScore.append(0)
                            avgScore.append(0)
                            gradeScore.append("N/A")
                            if st == "320-01":  # 처음 생성되는 계정이면 관리자 권한을 부여하게끔 만듦
                                group.append("Admin")
                            else:
                                while True:
                                    select = input("""
                                    ================================
                                    가입하시는 사용자의 역할을 선택하세요.
                                    1. 학생
                                    2. 교수
                                    3. 관리자
                                    """)
                                    if select == "1":      #딕셔너리로 권한 부여를 바꾸는 방법 있는지 찾기
                                        group.append("Student")
                                        print("생성하신 계정은 '학생용' 계정입니다.")
                                        break
                                    elif select == "2":
                                        group.append("Professor")
                                        print("생성하신 계정은 '교수용' 계정입니다.")
                                        break
                                    elif select == "3":
                                        adKey = input("관리자 확인용 비밀번호 4자리를 입력하세요: ")
                                        if adKey == "1004": #내부적으로 관리자들에게만 공유되고 변경되는 마스터키
                                            group.append("Admin")
                                            print("생성하신 계정은 '관리자용' 계정입니다.")
                                            break
                                        else:
                                            print("관리자 확인 비밀번호를 다시 입력하세요")
                            print("\n회원가입이 완료되었습니다.\n메뉴로 돌아갑니다.")
                            time.sleep(1)
                        else:
                            print("\n회원가입이 취소되었습니다.\n메뉴로 돌아갑니다.")
                            time.sleep(1)
                    break
# ------------------------------------------------------------------------------------------------------------
            # 1-3 회원수정 메뉴
            elif subSelect == "3":
                print("\n[회원수정 메뉴입니다.]")
                if session is None:
                    print("로그인 후 이용 가능합니다.")
                    continue
                sn = input("\n'320-00'형식으로 '-'를 포함하여\n본인의 학번 6자리를 입력하세요 :")  # 몇 자리를 입력해야 하는지 정해주는 표현식 찾기
                if sn in stuNum:
                    idx = stuNum.index(sn)
                    pw = input("본인의 패스워드를 입력하세요 :")
                    if passwords[idx] == pw:
                        print(f"\n{names[idx]}님 본인인증 확인되었습니다.\n수정할 내용을 입력해주세요.")
                        while True:
                            choice = input("\n수정하려는 회원정보를 선택하세요 : \n1. 이름 변경\n2. 이메일 변경\n3. 비밀번호 변경\n4. 계정 역할 변경\n9. 회원메뉴로 돌아가기")
                            if choice == "1":
                                names[session] = input("새 이름 : ")
                                print("이름 변경 완료 :" + names[session])
                            elif choice == "2":
                                emails[session] = input("새 이메일 : ")
                                print("이메일 변경 완료 :" + emails[session])
                            elif choice == "3":
                                passwords[session] = input("새 비밀번호 : ")
                                print("비밀번호 변경 완료 :" + passwords[session])
                            elif choice == "4":
                                while True:
                                    select = input("""
                                    ================================
                                    변경하려는 사용자 역할을 선택하세요.
                                    1. 학생
                                    2. 교수
                                    3. 관리자
                                    """)
                                    if select == "1":
                                        group[idx] = "Student"
                                        print("변경하신 계정은 '학생용' 계정입니다.")
                                        break
                                    elif select == "2":
                                        group[idx] = "Professor"
                                        print("변경하신 계정은 '교수용' 계정입니다.")
                                        break
                                    elif select == "3":
                                        adKey = input("관리자 확인용 비밀번호 4자리를 입력하세요: ")
                                        if adKey == "1004": #내부적으로 관리자들에게만 공유되고 변경되는 마스터키
                                            group[idx] = "Admin"
                                            print("변경하신 계정은 '관리자용' 계정입니다.")
                                            break
                                        else:
                                            print("\n관리자 확인 비밀번호가 틀렸습니다.\n사용자 역할을 다시 선택하세요.")
                                    else:
                                        print("\n잘못 입력하셨습니다. 사용자 역할을 다시 선택해주세요.")
                            elif choice == "9":
                                print("회원메뉴로 돌아갑니다.")
                                time.sleep(1)
                                break
                            else:
                                print("수정할 정보의 메뉴를 정확히 선택해주세요")
                    else:
                        print("\n비밀번호가 일치하지 않습니다.\n회원메뉴로 돌아갑니다.")
                        time.sleep(1)
                else:
                    print("\n입력하신 학번을 찾을 수 없습니다.\n회원메뉴로 돌아갑니다.")
                    time.sleep(1)
# ------------------------------------------------------------------------------------------------------------
            # 1-4 회원 탈퇴 메뉴
            elif subSelect == "4":
                if session is None:
                    print("\n로그인 후 이용 가능합니다.\n회원 메뉴로 돌아갑니다.")
                    time.sleep(1)
                    continue
                print("\n[회원탈퇴 메뉴에 진입하셨습니다.]")
                while True:
                    sn = input("\n'320-00'형식으로 '-'를 포함하여\n회원탈퇴할 학번을 입력 :")
                    if sn in stuNum:
                        idx = stuNum.index(sn)
                        pw = input("본인의 패스워드를 입력하세요 :")
                        if passwords[idx] == pw:
                            print(f"\n{names[idx]}님 본인인증 확인되었습니다.\n{names[idx]} 회원의 정보를 영구히 삭제합니다.")
                            if input("\n정말로 탈퇴하시겠어요? \n탈퇴를 희망하시면 'Enter'키를,\n메뉴로 돌아가려면 아무키나 누르세요('Enter'키 제외)") == "":
                                if len(sns) <= 1:
                                    print("\n최소 한 명의 회원은 있어야 합니다.\n다른 계정을 회원가입 후 탈퇴하세요!!")
                                    time.sleep(2)
                                    subRun = False
                                    break
                                if group.count("Admin") < 2: #관리자가 한 명만 있는 상황
                                    if group[idx] == "Admin":
                                        print("\n최소 한명의 관리자는 있어야합니다.\n다른 계정을 관리자로 승격 후 탈퇴하세요!!")
                                        time.sleep(2)
                                        subRun = False
                                        break
                                ids.pop(idx)
                                passwords.pop(idx)
                                emails.pop(idx)
                                group.pop(idx)
                                sns.pop(idx)
                                names.pop(idx)  # (배열관련 리스트에서 삭제할떄는 Pop이 좋고, "글자를 찾아서 지울 땐 remove를 쓴다.")
                                pythonScore.pop(idx)
                                dataBaseScore.pop(idx)
                                wwwScore.pop(idx)
                                totalScore.pop(idx)
                                avgScore.pop(idx)
                                gradeScore.pop(idx)
                                stuNum.pop(idx)
                                self_delete = (idx == session)  # 본인 계정을 삭제하는지를 확인하는 변수 맞을경우 로그아웃 시켜주기 위한 작업
                                if self_delete:
                                    print("\n로그인한 본인의 계정이 삭제되어 로그아웃 됩니다.\n메인 메뉴로 돌아갑니다.")
                                    session = None   #본인의 계정 삭제가 맞으면 로그아웃
                                    subRun = False
                                    time.sleep(2)
                                    break
                                elif idx < session:
                                    sns -= 1
                                else:
                                    print("\n회원탈퇴가 완료되었습니다.\n메인 메뉴로 돌아갑니다.")
                                    subRun = False
                                    time.sleep(2)
                                    break
                            else:
                                print("\n회원탈퇴를 취소합니다.\n회원메뉴로 돌아갑니다.")
                                time.sleep(1)
                                break
                        else:
                            print("\n비밀번호가 일치하지 않습니다.\n회원메뉴로 돌아갑니다.")
                            time.sleep(1)
                            break
                    else:
                        print("\n입력한 회원 정보를 찾을 수 없습니다.\n회원메뉴로 돌아갑니다.")
                        time.sleep(2)
                        break
# ------------------------------------------------------------------------------------------------------------
            # 1-9 회원 메뉴 종료
            elif subSelect == "9":
                print("\n회원 관리 메뉴를 종료 합니다.")
                subRun = False
                time.sleep(1)
            else:
                print("\n잘못된 메뉴를 선택하셨습니다.")
                time.sleep(1)
#######################################################################################################################
    elif select == "2":
        if session is None:
            print("\n로그인 후 이용 가능합니다.\n메뉴로 돌아갑니다.")
            time.sleep(1)
            continue
        print("\n성적관리 메뉴로 진입합니다.")
        subRun = True
        while subRun == True:
            print(scoreMenu)
            if session is not None:             #메인메뉴나 서브메뉴 진입시에 계속 사용자의 권한과 로그인 상태를 확인시켜서 꼬이는 게 있는지 확인하는 방법
                if group[session] == "Admin":
                    print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[관리자 권한]")
                elif group[session] == "Professor":
                    print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[교수 권한]")
                elif group[session] == "Student":
                    print(f" >>> 현재접속중: {names[session]} | 학번: {stuNum[session]}\n[학생 권한]")
                else:
                    print("외부 사용자 입니다.")
            subSelect = input("이용하시려는 회원메뉴 번호를 선택하세요.")
# ------------------------------------------------------------------------------------------------------------
            # 2-1 성적입력(교수전용) 메뉴
            if subSelect == "1":
                if group[session] == "Professor" or "Admin":
                    print("\n[성적입력(교수전용) 메뉴에 진입하셨습니다.]")
                    sn = input("\n'320-00'형식으로 '-'를 포함하여\n본인의 학번 6자리를 입력하세요 :")  # 몇 자리를 입력해야 하는지 정해주는 표현식 찾기
                    if sn in stuNum:
                        idx = stuNum.index(sn)
                        if group[idx] == "Student":
                            while True:
                                pys = int(input("\n파이썬 점수를 입력하세요. :"))  # 키보드로 입력한 숫자는 문자로 인식되므로 int()감사 계산용만듦
                                if 1 <= int(pys) <= 100:
                                    while True:
                                        dbs = int(input("영어 점수를 입력하세요. :"))
                                        if 1 <= int(dbs) <= 100:
                                            while True:
                                                www = int(input("수학 점수를 입력하세요. :"))
                                                if 1 <= int(www) <= 100:
                                                    print(
                                                        f"\n학번 : {stuNum[idx]} | 이름 : {names[idx]} | 파이썬 : {pys} | 데이타베이스 : {dbs} | 프론트 : {www}")
                                                    if input(
                                                            "\n입력한 성적을 저장하시려면 \n'Enter'를 누르시고\n취소하시려면 아무키나 누르세요('Enter'키 제외)") == "":
                                                        pythonScore[idx] = pys
                                                        dataBaseScore[idx] = dbs
                                                        wwwScore[idx] = www
                                                        tot = pys + dbs + www
                                                        totalScore[idx] = tot
                                                        avgScore[idx] = (tot / 3)
                                                        if (tot / 3) >= 90:
                                                            gradeScore[idx] = "A"
                                                        elif (tot / 3) >= 80:
                                                            gradeScore[idx] = "B"
                                                        elif (tot / 3) >= 70:
                                                            gradeScore[idx] = "C"
                                                        elif (tot / 3) >= 60:
                                                            gradeScore[idx] = "D"
                                                        else:
                                                            gradeScore[idx] = "F"
                                                        print("\n성적 입력이 저장되었습니다. \n성적 관리 메뉴로 돌아갑니다.")
                                                        time.sleep(2)
                                                        break
                                                    else:
                                                        print("\n성적 입력이 취소되었습니다. \n성적관리 메뉴로 돌아갑니다.")
                                                        time.sleep(2)
                                                    break
                                                else:
                                                    print("수학점수 입력값을 다시 확인하세요.")
                                            break
                                        else:
                                            print("영어점수 입력값을 다시 확인하세요.")
                                    break
                                else:
                                    print("파이썬점수 입력값을 다시 확인하세요.")
                        else:
                            print("\n학생의 성적만 입력 가능합니다.\n입력한 학번은 학생이 아닙니다.")
                            time.sleep(2)
                    else:
                        print("\n입력한 회원 정보를 찾을 수 없습니다.\n성적관리 메뉴로 돌아갑니다.")
                        time.sleep(1)
                else:
                    print("\n교수님 전용 메뉴입니다.\n계정 권한을 확인하세요")
                    subRun = False
                    time.sleep(1)
                    break
# ------------------------------------------------------------------------------------------------------------
            # 2-1 성적보기 (학생이냐 교수or관리자냐에 따라 학생의 성적이 다르게 노출됨)
            elif subSelect == "2":
                if group[session] == "Student":
                    print("\n[성적보기(학생용) 메뉴에 진입하셨습니다.]")
                    sn = input("\n'320-00'형식으로 '-'를 포함하여\n본인의 학번 6자리를 입력하세요 :")  # 몇 자리를 입력해야 하는지 정해주는 표현식 찾기
                    if sn in stuNum:
                        idx = stuNum.index(sn)
                        pw = input("본인의 패스워드를 입력하세요 :")
                        if passwords[idx] == pw:
                            print(f"\n{names[idx]}님 본인인증 확인되었습니다.\n")
                            if totalScore[idx] == 0:
                                print("\n입력된 성적이 없습니다.\n.교수님께 문의하세요\n'010-4872-4872':(")
                                time.sleep(5)
                                subRun = False
                                break
                            else:
                                print(f"조회하신 {names[idx]}님의 점수는 다음과 같습니다.")
                                print(f"파이썬 점수: {pythonScore[idx]}\n데이타베이스 점수: {dataBaseScore[idx]}\n프론트 점수: {wwwScore[idx]}\n총점: {totalScore[idx]}\n평균: {avgScore[idx]}\n등급: {gradeScore[idx]}")

                                if input("\n이전 메뉴로 돌아가시려면 'Enter'키를 눌러주세요") == "":
                                    print("성적관리 메뉴로 돌아갑니다.")
                                    time.sleep(1)
                                else:
                                    print("\n'Enter'키를 정확히 입력해주세요.")


                        else:
                            print("\n입력한 패스워드가 맞지 않습니다.\n성적 관리 메뉴로 돌아갑니다.")
                            time.sleep(2)
















                break

            elif subSelect == "9":
                print("\n성적 관리 메뉴를 종료 합니다.")
                subRun = False
                time.sleep(1)















    elif Select == "3":
        pass

    elif Select == "4":
        pass


    elif select == "9":
        print("\nMBC 아카데미 LMS 프로그램을 종료합니다.\n다음에 또 만나요!")
        time.sleep(2)
        run = False
    else:
        print("\n잘못된 메뉴를 선택하셨습니다.")
        time.sleep(1)