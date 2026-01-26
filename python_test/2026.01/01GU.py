# 목표 : MBC아카데미 LMS 프로그램을 만들어 보자.
# 회원관리 : 시스템담당자, 교수, 행정, 학생, 손님, 학부모
# 성적관리 : 교수가성정등록,수정,
#           행정담당자가 학기마다 백업(이전->삭제)
#           학생은 개인성적일람, 성적출력
#           손님은 학교소개페이지 열람
#           학부모는 자녀학사관리
# 게시판 : 회원제, 비회원제, 문의사항, Q/A

# 필요한 변수
run = True # 메인 메뉴용 while
# subRun = True # 보조 메뉴용 while
session = None # 로그인한 사용자의 인덱스를 기억

# 필요한 리스트
# 회원에 대한 리스트
sns = [1] # 회원에 대한 번호
ids = ["kkw"] # id에 대한 리스트
pws = ["1234"] # 암호에 대한 리스트
group = ["pro"] # 회원등급
# admin (관리자), stu(학생), guest(손님)...

# 성적에 대한 리스트
pythonScore =[] # 파이썬 점수들
databaseScore = [] # 데이터베이스 점수들
wwwScore = [] # 프론트 점수들
totalScore = [] # 총점들
avgScore = [] # 평균들
gradeScore = [] # 등급들

stuIdx = {} # 학생의 인덱스 (학번) <-> 회원의 sns
# 회원가입 할때마다 회원번호 인덱스는 늘어남
# 그러나 학생 인덱스는 늘어나지 않음 왜냐면 학생수만큼 늘어나기에
# 학생 인덱스를 어떻게 조회해서 핀포인트로 점수를 넣어줄수있나

# 회원번호 받아서 성적 입력
# 회원번호를 받아서 딕셔너리 키 값으로 지정후 밸류에 성적 리스트들 입력
# 회원 삭제될때 키 값을 불러와 파이썬 디비 프론트등 한번에 삭제
# 밸류에는 리스트도 들어가기 가능

# 딕셔너리 키 밸류로 해서
# 학생 인덱스 (ex 4학번) 4: [100,80,90]
# stuIdx = { sns[idx] : [100,80,30] }
# stuIdx[sns[idx]] = [py,db,www]
# 회원번호는 고유하니까 키값으로 사용 가능


# 게시판에 대한 리스트
board_no = [] # 게시물의 번호
board_title = [] # 게시물의 제목
board_content = [] # 게시물의 내용
board_writer = [] # 게시물 작성자 <-> 회원의 sns
boardIdx = {}

# 메뉴 구성
mainMenu = """
=================================
엠비씨아카데미 LMS에 오신걸 환영합니다.

1. 로그인(회원가입)
2. 성적관리
3. 게시판
4. 관리자메뉴
9. 프로그램종료
"""

memberMenu = """
---------------------------------
회원관리 메뉴입니다.

1. 로그인
2. 회원가입
3. 회원수정
4. 회원탈퇴

9. 회원관리 메뉴 종료
"""

scoreMenu = """
----------------------------------
성적관리 메뉴입니다.

1. 성적입력(교수전용)
2. 성적보기(개인용)
3. 성적수정(교수전용)
4. 성적백업(행정직원전용)

9. 성적관리 메뉴 종료
"""

boardMenu = """
-----------------------------------
회원제 게시판 입니다.

1. 게시글 작성
2. 게시글 수정
3. 게시글 검색
4. 게시글 삭제

9. 게시판 메뉴 종료
"""


# 주 실행문 구현
while run :
    print(mainMenu) # 메인메뉴 출력용
    select = input("메뉴를 선택 : ")
    if select == "1" :
        print("로그인(회원가입) 메뉴로 진입합니다.")



        # 메인 메뉴
        while run :
            print(memberMenu)
            subSel = input("메뉴선택 : ")
            # 로그인
            if subSel == "1" :

                # 방어코드 이미 로그인중이면 못들어오게
                if session is not None:
                    print(f"이미 로그인중입니다.\t 현재 로그인 중인 아이디 : {session}") # 수정필요 정보수정하고 로그인하면 반영 안됨
                    continue

                print("로그인 메뉴로 진입합니다.")
                session = input("아이디를 입력해주세요 : ")
                if session in ids :
                    idx = ids.index(session) # 현재 아이디의 주소값
                    pw = input("비번 : ")
                    if pw in pws[idx] :
                        print("로그인되셨습니다.")
                    else :
                        print("비밀번호 오류")
                else :
                    print("아이디 오류.")

            # 회원가입
            elif subSel == "2" :
                print("회원가입 메뉴로 진입합니다.")
                id = input("사용하실 아이디 : ")
                pw = input("사용하실 비번 : ")

                print(f"아이디 : {id}\t 비밀번호 : {pw}")
                choose = input("맞다면 y : ")
                if choose == "y" :
                    sns.append(len(sns)+1)
                    ids.append(id)
                    pws.append(pw)
                    group.append("user")
                    idx = ids.index(id)
                    print(f"회원번호 : {sns[idx]}, 아이디 : {ids[idx]} 비번 : {pws[idx]}, 등급 : {group[idx]}")
                else:
                    print("이전 메뉴로 돌아갑니다.")

            # 회원 수정
            elif subSel == "3" :
                print("회원 수정 메뉴로 진입합니다.")

                # 방어코드
                if session is None :
                    print("로그인 후 이용해주세요")
                else:
                    print("수정하실 정보 입력")
                    idx = ids.index(session)
                    ids[idx] = input("아이디 수정 : ")
                    pws[idx] = input("비밀번호 수정 : ")
                    session = ids[idx]
                    print(f"수정된 아이디 : {ids[idx]}, 수정된 비번 : {pws[idx]}")
                    print("수정완료")

            elif subSel == "4" :
                print("회원 탈퇴 메뉴로 진입합니다.")
                if session is None :
                    print("로그인 후 이용해주세요")
                else :
                    print("회원 탈퇴 메뉴입니다.")
                    idx = ids.index(session)

                    print(f"\t 아이디 : {ids[idx]}, 비밀번호 : {pws[idx]} ")
                    choose = input("탈퇴 원하면 y : ")
                    if choose == "y" :
                        sns.pop(idx)
                        ids.pop(idx)
                        pws.pop(idx)
                        group.pop(idx)
                        print("탈퇴하셨습니다.")
                        session = None
                    else :
                        print("다시 입력해주세요")


            elif subSel == "9" :
                print("회원 관리 메뉴를 종료합니다.")
                break
            else : # 1,2,3,4,9 말고 다른 키를 넣을 경우
                print("잘못된 메뉴를 선택하였습니다.")

    elif select == "2" :
        while run :

            if session is None:
                print("로그인 후 이용해주세요")
                break

            print(scoreMenu)
            select = input("메뉴 선택 : ")

            if select == "1" :
                idx = ids.index(session) # 현재 아이디의 주소값으로 교수인지 판단
                if group[idx] == "pro" :
                    print("성적입력(교수용)")
                    sn = int(input("점수입력할 회원번호 : "))
                    if sn in sns :
                        snIndex = sns.index(sn) # 수정할 회원의 주소값
                        py = int(input("파이썬 점수를 입력해주세요 : "))
                        db = int(input("DB 점수를 입력해주세요 : "))
                        www = int(input("프론트 점수를 입력해주세요 : "))
                        tot = py + db +www
                        avg = tot/3

                        print(f"파이썬 : {py}, DB : {db}, www : {www}")
                        choose = input("맞다면 y : ")
                        if choose == "y" :
                            if avg >= 90:
                                grade = "A"
                            elif avg >= 80 :
                                grade = "B"
                            elif avg >= 70 :
                                grade = "C"
                            else :
                                grade = "F"
                            # pythonScore.append(py)
                            # databaseScore.append(db)
                            # wwwScore.append(www)
                            # totalScore.append(tot)
                            # avgScore.append(avg)
                            # gradeScore.append(grade)
                            stuIdx = {sns[snIndex] : [py,db,www,tot,avg,grade]}
                            print("입력완료")
                            print(stuIdx[sn])

                    else :
                        print("존재하지 않는 번호입니다.")
                else:
                    print("교수전용입니다.")
                    break

            elif select == "2" :
                print("성적보기(개인용)")
                idx = ids.index(session)

                if group[idx] == "pro" :
                    print(f"{ids[idx]}님")
                    if sns[idx] in stuIdx:
                        print(f"파이썬 : {stuIdx[sns[idx]][0]} DB : {stuIdx[sns[idx]][1]} 프론트 : {stuIdx[sns[idx]][2]}"
                              f" 등급 : {stuIdx[sns[idx]][5]}")

                    else:
                        print("점수가 존재하지 않습니다.")

            elif select == "3" :
                idx = ids.index(session)  # 현재 아이디의 주소값으로 교수인지 판단
                if sns[idx] in stuIdx:
                    if group[idx] == "pro":
                        print("성적수정(교수용)")
                        sn = int(input("수정할 회원번호 : "))

                        snDic = sn # 딕셔너리 출력용
                        if sn in sns:
                            snIndex = sns.index(sn)  # 수정할 회원의 주소값
                            print("수정할 점수를 입력하세요")
                            py = int(input("파이썬 점수를 입력해주세요 : "))
                            db = int(input("DB 점수를 입력해주세요 : "))
                            www = int(input("프론트 점수를 입력해주세요 : "))
                            tot = py + db + www
                            avg = tot / 3

                            print(f"파이썬 : {py}, DB : {db}, www : {www}")
                            choose = input("맞다면 y : ")
                            if choose == "y":
                                if avg >= 90:
                                    grade = "A"
                                elif avg >= 80:
                                    grade = "B"
                                elif avg >= 70:
                                    grade = "C"
                                else:
                                    grade = "F"
                            else:
                                print("다시입력해주세요")
                            sn = stuIdx.pop(sn)
                            stuIdx = {sns[snIndex]: [py, db, www, tot, avg, grade]}
                            print("입력완료")
                            print(stuIdx[snDic])
                        else:
                            print("다시입력해주세요")

                    else:
                        print("교수전용입니다.")
                else:
                    print("성적이 존재하지 않습니다.")


            elif select == "4" :
                idx = ids.index(session)
                if sns[idx] in stuIdx:
                    if group[idx] == "pro":
                        print("성적백업(행정직원용)")
                        backUp = {} # 백업용 딕셔너리 변수
                        sn = int(input("백업할 회원번호 : "))
                        if sn in stuIdx:
                            backUp[sn] = stuIdx.pop(sn)
                            print("백업완료")
                        else:
                            print("번호를 다시 확인해주세요")
                    else:
                        print("교수전용입니다.")
                else:
                    print("백업할 성적이 존재하지 않습니다.")

            elif select == "9" :
                print("성적관리 메뉴 종료")
                break
            else:
                print("다시 입력")


    elif select == "3" :

        if session is None:
            print("로그인 후 이용해주세요")
            continue

        while run :
            print(boardMenu)
            select = input("1~4선택 : ")
            idx = ids.index(session)
            if select == "1" :
                print("게시글 작성")
                no = len(boardIdx)+1
                title = input("제목을 입력해주세요 : ")
                content = input("내용을 입력해주세요 : ")
                writer = ids[idx]
                print(f"제목 : {title} 내용 : {content} 작성자 : {writer}")

                choose = input("맞으면 y : ")
                if choose == "y" :
                    boardIdx = {sns[idx]: [no, title, content, writer]}
                    print("작성 완료")
                else:
                    print("다시입력하세요")


            elif select == "2" :
                pw = input("수정하시려면 비번을 입력하세요 : ")

                if pw in pws[idx] :
                    no = boardIdx[sns[idx]][0]
                    del boardIdx[sns[idx]]
                    title = input("수정할 제목을 입력해주세요 : ")
                    content = input("수정할 내용을 입력해주세요 : ")
                    writer = ids[idx]

                    print(f"제목 : {title} 내용 : {content} 작성자 : {writer}")

                    choose = input("맞으면 y : ")
                    if choose == "y":
                        boardIdx = {sns[idx]: [no, title, content, writer]}
                        print("수정 완료")
                        print(f"{boardIdx}")
                    else:
                        print("다시입력하세요")
                else:
                    print("비밀번호가 틀립니다.")

            elif select == "3" :
                if sns[idx] in boardIdx:
                    print(f"글 번호 : {boardIdx[sns[idx]][0]}\t 제목 : {boardIdx[sns[idx]][1]}\t 내용 : {boardIdx[sns[idx]][2]}"
                          f" 작성자 : {boardIdx[sns[idx]][3]}")
                else:
                    print("게시글이 존재하지 않습니다.")
            elif select == "4" :
                pw = input("삭제하시려면 비번을 입력하세요 : ")
                if pw in pws[idx] :
                    del boardIdx[sns[idx]]
                    print("삭제 완료")
                else:
                    print("비번이 틀림")


            elif select == "9" :
                print("게시판 메뉴 종료")
                break
            else :
                print("1~4 선택해주세요")

    elif select == "4" :
        ""
    elif select == "9" :
        run = False
    else:
        print("다시 입력해주세요")