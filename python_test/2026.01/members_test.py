# TXT 파일을 생성하기

import os
run = True # while 프로그램 시작/종료(메인메뉴)
subrun =True # while 프로그램 시작/종료(서브메뉴)
session =None # 회원의 로그인 상태

# C 생성 => 회원가입 회원의 계정을 생성함
# R 리스트 => 회원의 리스트를 전체로 보기
# R 리스트 => 1명의 회원의 정보를 볼 수 있게 리스트를 가져오기
# U 수정 => Txt 파일을 덮어써야하기 때문에 기존의 회원의 정보를 수정하고 덮어쓴다.
# D 삭제 => Txt 파일을 덮어써야하기 때문에 기존의 회원 정보를 비활성화하고 덮어쓴다.
FILE_NAME = "members2.txt"
FILE_NAME2 = "scores.txt"
FILE_NAME3 = "boards.txt"
FILE_NAME4 = "login_data.txt"

members = []
scores = []
boards = []
login_datas=[]

def save_members():
    with open(FILE_NAME,"w",encoding="utf8") as f:
        for member in members:
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}|{member[5]}|{member[6]}\n"
            #           ID          PW          이름       생년월일         연락처       권한         활성화
            f.write(line)
# 회원 저장 함수
def save_scores():
    with open(FILE_NAME2,"w",encoding="utf8") as f:
        for score in scores:
            line2 = f"{score[0]}|{score[1]}|{score[2]}|{score[3]}|{score[4]}|{score[5]}|{score[6]}\n"
            #          파이썬       DB       프론트        총점        평균        등급        이름
            f.write(line2)
# 성적 저장 함수
def save_boards():
    with open(FILE_NAME3,"w",encoding="utf8") as f:
        for board in boards:
            line3 = f"{board[0]}|{board[1]}|{board[2]}|{board[3]}|{board[4]}|{board[5]}\n"
            #          게시글번호    제목        내용       작성자       조회수      좋아요
            f.write(line3)
# 게시글 저장 함수
def save_login_data():
    global session
    if session is None:
        return

    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME4,"a",encoding="utf8") as f:
        line4 =f"{now}|[LOGIN]|{members[session][0]}\n"
            #        날짜 시간 로그인ID 또는 로그아웃 ID
        f.write(line4)

def save_logout_data():

    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME4,"a",encoding="utf8") as f:
        line4 =f"{now}|[LOGOUT]|{members[session][0]}\n"
            #        날짜 시간 로그인ID 또는 로그아웃 ID
        f.write(line4)


def load_members():

    if not os.path.exists(FILE_NAME):
        save_members()
        return

    with open(FILE_NAME,"r",encoding="utf8") as f:
        for line in f:
            data = line.strip().split("|")
            data[3] = int(data[3])
            if data[6] == "True":
                data[6] = True
            else:
                data[6] = False


            members.append(data)

def load_scores():
    if not os.path.exists(FILE_NAME2):
        save_scores()
        return
    with open(FILE_NAME2,"r",encoding="utf8") as f:
        for line2 in f:
            data2 = line2.strip().split("|")
            data2[0] = int(data2[0])
            data2[1] = int(data2[1])
            data2[2] = int(data2[2])
            data2[3] = int(data2[3])
            data2[4] = float(data2[4])

            scores.append(data2)

def load_boards():
    if not os.path.exists(FILE_NAME3):
        save_boards()
        return
    with open(FILE_NAME3,"r",encoding="utf8") as f:
        for line3 in f:
            data3 = line3.strip().split("|")
            data3[0] = int(data3[0])
            data3[4] = int(data3[4])
            data3[5] = int(data3[5])

            boards.append(data3)

def member_add():
    print("""
    ==========================================
                MBC 아카데미 회원가입 
    ------------------------------------------
    MBC 회원가입 페이지입니다. 
    """)
    new_id = input(" ▶ 아이디 : ")
    for member in members:
        if member[0] == new_id:
            print(" ▶ 이미 존재하는 아이디입니다.")
            return
    new_pw = input(" ▶ 비밀번호 : ")
    new_name = input(" ▶ 이름 : ")
    new_age = input(" ▶ 생년월일 ex)20090102 : ")
    new_number = input(" ▶ 연락처 ex)010-1234-1234 : ")
    print(f"""
    입력하신 정보를 확인 후 저장번호를 입력해주세요!
    |1| 이름 : {new_name}
    |2| 생년월일 : {new_age}
    |3| 연락처 : {new_number}
    |4| 아이디 : {new_id}
    |5| 비밀번호 : {new_pw}
    ------------------------------------------
    |1|저장        |2|취소
    """)
    save_add =input(" ▶▶▶ ")
    if save_add == "1":
        members.append([new_id,new_pw,new_name,new_age,new_number,"user",True])
        save_members()
    elif save_add == "2":
        return


def member_login():
    print("""
    ==========================================
                 MBC 아카데미 로그인
    ------------------------------------------
    """)
    global session
    global subrun
    uid = input(" ▶ 아이디 : ")
    upw = input(" ▶ 비밀번호 : ")

    for i,member in enumerate(members):

        if member[0] == uid:
            if member[6] is False:
                print(" ▶ 로그인 비활성화 계정입니다.")
                subrun = False
                return

            if member[1] == upw:
                print(f" ▶ {member[2]} 님 로그인되었습니다.")
                session = i
                save_login_data()
                return

            else:
                print(" ▶ 비밀번호가 맞지 않습니다.")
                subrun = False
                return
        else:
            pass

    print("등록되지 않은 아이디입니다.")
    subrun = False
    return



def my_scores():
    my_name = members[session][2]
    for i,score in enumerate(scores):
        if scores[i][6] == my_name:
            print(f"""
    ==========================================
                MBC 아카데미 내성적조회 
    ------------------------------------------
    ✓ 이름 :{members[session][2]}
    ✓ 파이선 :{scores[i][0]}ㅣ점 ✓ 데이터베이스 :{scores[i][1]}점
    ✓ 프론트: {scores[i][2]} |✓ 총점 :{scores[i][3]}점
    ✓ 평  균 :{scores[i][4]}점| ✓ 등급 :{scores[i][5]}등급
    ------------------------------------------""")
            return

def member_mypage():
    print(f"""
    ==========================================
                MBC 아카데미 마이페이지 
    ------------------------------------------
    ✓ 이름 :{members[session][2]}
    ✓ 생년월일 :{members[session][3]}
    ✓ 연락처 : {members[session][4]}
    ------------------------------------------
    |1| 연락처변경        |2| 회원탈퇴
    """)
    save_add = input(" ▶▶▶ ")
    if save_add == "1":
        num_sve = input("""
    ==========================================
                MBC 아카데미 내정보수정 
    ------------------------------------------
    변경하실 연락처를 입력해주세요!
▶▶▶ """)
        members[session][4] = num_sve
        save_members()
        return
    elif save_add == "2":
        member_del = input("""
    ==========================================
                MBC 아카데미 회원탈퇴
    ------------------------------------------
    회원탈퇴를 하시겠습니까?
    |1| 네              |2|아니요
▶▶▶ """)
        if member_del == "1":
            print("회원탈퇴가 완료되었습니다.")
            members[session][6] = False
            save_members()
            return
        elif member_del == "2":
            print("회원탈퇴가 취소되었습니다.")
            return


def member_list_score():
    if scores == []:
        print("등록된 성적이 없습니다.\n등록 후 확인해주세요! ")
        return
    else:
        print(f"""
    ==========================================
              MBC 아카데미 성적리스트 
    ------------------------------------------""")
    for i in range(len(scores)):
        print(f"""
    [NO].{i+1}
    ✓ 이름 :{scores[i][6]}|✓ 총점 :{scores[i][3]}점
    ✓ 평  균 :{scores[i][4]}점| ✓ 등급 :{scores[i][5]}등급
    ------------------------------------------""")

def member_save_score():
    member_list_score()
    search = input("""
    조회하실 학생의 이름을 입력해주세요!
▶▶▶ """)

    for i,member in enumerate(members) :
        if member[2] == search:
            print(f"{member[2]} 학생의 성적관리")
            print("---------------------")
            sel =input("""
    |1| 등록        |2| 수정       |3|삭제
▶▶▶ """)
            if sel == "1":
                print(f"{member[2]}학생의 성적등록")
                py_sve = int(input(" ▶ 파이썬 :"))
                db_sve = int(input(" ▶ 데이터페이스 :"))
                ww_sve = int(input(" ▶ 프론트 :"))

                #총점,평균,등급 계산
                total = py_sve+db_sve+ww_sve
                avg = total/3
                if avg >= 90:
                    grade ="A"
                elif avg >= 80:
                    grade ="B"
                elif avg >= 70:
                    grade ="C"
                elif avg >= 60:
                    grade ="D"
                else:
                    grade ="F"

                sve_sel = input(f"""
    -----------------------------------------
    입력하신 정보를 확인 후 [등록]번호를 입력해주세요!
     ▶ 파이썬 :{py_sve}|▶ 데이터페이스 :{db_sve}
     ▶ 프론트:{ww_sve}|▶ 총점:{total}
     ▶ 평균:{avg}|▶ 등급:{grade}
     ----------------------------------------
     |1| 등록        |2| 취소
▶▶▶ """)
                if sve_sel == "1":
                    print(f"    {member[2]}학생의 성적이 등록되었습니다.")
                    scores.append([py_sve,db_sve,ww_sve,total,avg,grade,member[2]])

                    #"{score[0]}|{score[1]}|{score[2]}|{score[3]}|{score[4]}|{score[5]}|{score[6]}\n"
                    #    파이썬       DB       프론트        총점        평균        등급        ID
                    save_scores()
                    return
                elif sve_sel == "2":
                    print("성적등록이 취소되었습니다.")
                break

            elif sel == "2":
                for i,score in enumerate(scores):
                    if score[6] == member[2]:

                        #for idx2,scores in members[idx][2]
                        print(f"{member[2]}학생의 성적수정")
                        py_sve = int(input(" ▶ 파이썬 :"))
                        db_sve = int(input(" ▶ 데이터페이스 :"))
                        ww_sve = int(input(" ▶ 프론트 :"))

                        # 총점,평균,등급 계산
                        total = py_sve + db_sve + ww_sve
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

                        sve_sel = input(f"""
    -----------------------------------------
    입력하신 정보를 확인 후 [저장]번호를 입력해주세요!
     ▶ 파이썬 :{py_sve}|▶ 데이터페이스 :{db_sve}
     ▶ 프론트:{ww_sve}|▶ 총점:{total}
     ▶ 평균:{avg}|▶ 등급:{grade}
     ----------------------------------------
     |1| 저장        |2| 취소
▶▶▶ """)
                        if sve_sel == "1":
                            print(f"    {member[2]}학생의 성적이 수정되었습니다.")
                            scores[i]=([py_sve, db_sve, ww_sve, total, avg, grade, member[2]])

                            # "{score[0]}|{score[1]}|{score[2]}|{score[3]}|{score[4]}|{score[5]}|{score[6]}\n"
                            #    파이썬       DB       프론트        총점        평균        등급        ID
                            save_scores()
                            return
                        elif sve_sel == "2":
                            print("     성적등록이 취소되었습니다.")
                        break




def member_score(): # 미완성 /미검증
    for idx,scores[6] in enumerate(members[session][0]) :
        print(f"""
    ==========================================
                MBC 아카데미 내성적 
    ------------------------------------------
    ✓ 이름 :{members[session][2]}
    ✓ 파이썬 :{scores[0]}점
    ✓ 데이터베이스 :{scores[1]}점
    ✓ 프론트 :{scores[2]}점
    ✓ 총점 :{scores[3]}점
    ✓ 평균 :{scores[4]}점
    ✓ 등급 :{scores[5]}등급
    """)
def list_boards():
    print(f"""
    ==========================================
                MBC 아카데미 게시판 
    ------------------------------------------""")

    for i,board in enumerate(boards):
        print(f"""
    N0.{board[0]}
    제목 :{board[1]}|작성작 :{board[3]}
    조회수:{board[4]}|좋아요:{board[5]}
    ------------------------------------------""")

    list_bor=int(input(f"""
    게시물 자세히 보기|게시물의 번호를 입력해주세요!
    [0] 다음
▶▶▶ """))

    if list_bor == board[0]:
        board[4] += 1
        save_boards()
        print(f"""
    N0.{board[0]}
    제목 :{board[1]}|작성작 :{board[3]}
    내용 : {board[2]}
    조회수:{board[4]}|좋아요:{board[5]}
    ------------------------------------------""")


    new_boa =input(f"""
    |1| 새글작성    |2| 좋아요     |3| 뒤로가기
▶▶▶ """)
    if new_boa == "1":
        print(f"""
    ==========================================
                MBC 아카데미 새글등록 
    ------------------------------------------""")
        new_no = len(boards)
        new_no +=1
        new1 =new_no
        new2 = input(" ▶ 게시글 제목 : ")
        new3 = input(" ▶ 게시글 내용 : ")
        new4 = members[session][2]

        save_add = input("""
    ----------------------------------------
     |1| 저장        |2| 취소
    ▶▶▶ """)
        if save_add == "1":
            print("게시글이 등록되었습니다.")
            boards.append([new1,new2,new3,new4,0,0])
            save_boards()
            return
        elif save_add == "2":
            print("게시글 등록이 취소되었습니다.")
            return
    elif new_boa == "2":
        board[5] +=1
        save_boards()
        return
    elif new_boa == "3":
        return
    else:
        return

def member_set():
    print(f"""
    ==========================================
           MBC 아카데미 프로그램 권한설정 
    ------------------------------------------
    회원의 권한을 설정할 수 있습니다.
    """)
    for i,member in enumerate(members):
        print(f"""N0.{i+1} 이름 : {member[2]} 
    ------------------------------------------""")


    sel = int(input("""
    회원의 번호를 입력해주세요!
▶▶▶ """))

    if sel == "0":
        print("잘못입력되었습니다.")
        return

    sel = sel - 1

    change=input(f"""
    {members[sel][2]}님 변경하실 권한을 선택해주세요!
    |1| 관리자         |2|일반회원
▶▶▶ """)
    if change == "1":
        members[sel][5] = "admin"
        print("관리자로 변경되었습니다.")
        return

    elif change == "2":
        members[sel][5] = "user"
        print("일반회원으로 변경되었습니다.")
        return


def member_blacklist():
    print(f"""
    ==========================================
           MBC 아카데미 학생관리 블랙리스트
    ------------------------------------------""")

    for i, member in enumerate(members):
        print(f"""N0.{i + 1} 이름 : {member[2]}
    ------------------------------------------""")

    sel = int(input("""
        회원의 번호를 입력해주세요!
▶▶▶ """))
    if sel =="0":
        print("잘못입력되었습니다.")
        return

    sel=sel-1

    change = input(f"""
    {members[sel][2]}님을 블랙리스트로 설정하시겠습니까?
    |1| 블랙리스트         |2|일반회원
▶▶▶ """)
    if change == "1":
        members[sel][6] = False
        save_members()
        print("블랙리스트로 변경되었습니다.")
        return

    elif change == "2":
        members[sel][6] = True
        save_members()
        print("일반회원으로 변경되었습니다.")
        return

def main_menu_logout():
    print("""
    ==========================================
           MBC 아카데미 학생관리 프로그램 
    ------------------------------------------
    
    |1| 로그인           |2| 회원가입
    
    ------------------------------------------
    |0| 프로그램종료
    """)

def main_menu_login():
    print("""
    ==========================================
           MBC 아카데미 학생관리 프로그램 
    ------------------------------------------

    |1| 마이페이지        |2| 내성적보기
    |3| 게시판        
        
    ------------------------------------------
    |9|로그아웃          |0| 프로그램종료
    """)


def main_menu_login_admin():
    print("""
    ==========================================
           MBC 아카데미 학생관리 프로그램 
    ------------------------------------------

    |1| 마이페이지       |2| 성적조회/등록
    |3| 게시판          |4| 권한설정 
    |5| 블랙리스트       

    ------------------------------------------
    |9|로그아웃          |0| 프로그램종료
    """)

load_members()
load_scores()
load_boards()

while run:
    main_menu_logout()
    if session == None:
        print("[비회원]계정입니다.\n[로그인] 후 이용해주세요!")
    else:
        print(f"{members[session][2]}님은 \n{members[session][5]}계정입니다.")

    select = input(" ▶▶▶ ")
    if select == "1":
        subrun = True
        member_login()
        while subrun:
            if members[session][5] == "admin":
                main_menu_login_admin()
                print(f"{members[session][2]}님은 \n{members[session][5]}계정입니다.")
                select = input(" ▶▶▶ ")
                if select == "1":
                    member_mypage()
                elif select == "2":
                    member_save_score()
                elif select == "3":
                    list_boards()
                elif select == "4":
                    member_set()
                elif select == "5":
                    member_blacklist()
                elif select == "9":
                    save_logout_data()
                    session=None
                    subrun = False
                elif select == "0":
                    subrun = False
                    run = False

            elif members[session][5] == "user":
                main_menu_login()
                print(f"{members[session][2]}님은 \n{members[session][5]}계정입니다.")
                select = input(" ▶▶▶ ")
                if select == "1":
                    member_mypage()
                elif select == "2":
                    my_scores()
                elif select == "3":
                    list_boards()
                elif select == "9":
                    save_logout_data()
                    session=None
                    subrun = False
                elif select == "0":
                    subrun = False
                    run = False

    elif select == "2":
        member_add()
    elif select == "0":
        print("""
        ==========================================
              MBC 아카데미 학생관리 프로그램 종료 
        ------------------------------------------
        """)
        run = False

