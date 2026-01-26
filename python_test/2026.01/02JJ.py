# 대부분 프로그래밍에서 1번이 되는(start) 파일을 main 으로 만듬

# 목표 : MBC아카데미 LMS 프로그램을 만들어 보자.
# 회원관리 : 시스템담당자(admin), 교수(professor), 행정직원(employee), 학생(stu), 손님(guest), 학부모(parent)
# 성적관리 : 교수가 성적 등록, 수정,
#          행정담당자가 학기마다 백업(이전->삭제)
#          학생은 개인성적일람, 성적 출력
#          손님은 학교소개페이지 열람
#          학부모는 자녀학사관리
# 게시판 : 회원제, 비회원제, 문의사항, Q/A

# 필요한 변수
run = True # 메인 메뉴용 while
# subRun = True # 보조 메뉴용 while
session = None # 로그인한 사용자의 인덱스를 기억

# 필요한 리스트
# 회원에 대한 리스트
sns = [1] # 회원에 대한 번호
ids = ['kkw'] # id에 대한 리스트
pws = ['1234'] # 암호에 대한 리스트
group = ['admin'] # 회원등급
# admin(관리자), stu(학생), guest(손님) ....

# 성적에 대한 리스트
pythonScore = [] #파이썬 점수들
databaseScore = [] # 데이터베이스 점수들
wwwScore = [] # 프론트 점수들
totalScore = [] # 총점 들
avgScore = [] # 평균 들
gradeScore = [] # 등급 들
stuIdx = [] # 학생의 인덱스 (학번) <-> 회원의 sns

# 게시판에 대한 리스트
board_no = [] # 게시물의 번호
board_title = [] # 게시물의 제목
board_content = [] # 게시물의 내용
board_writer = [] # 게시물 작성자 <-> 회원의 sns

# 메뉴 구성
mainMenu = """
===========================
엠비씨아카데미 LMS에 오신걸 환영합니다.

1. 로그인(회원가입)
2. 성적관리
3. 게시판
4. 관리자메뉴
9. 프로그램 종료
"""

memberMenu = """
===========================
회원관리 메뉴입니다.

1. 로그인
2. 회원가입
3. 회원수정
4. 회원탈퇴

9. 회원관리 메뉴 종료

"""

scoreMenu = """
--------------------------
성적관리 메뉴입니다.

1. 성적입력(교수전용)
2. 성적보기(개인용)
3. 성적보기(교수전용)
4. 성적백업(행정직원전용)

9. 성적관리 메뉴 종료 
"""

boardMenu = """
------------------------
회원제 게시판 입니다.

1. 게시판 등록
2. 게시판 목록
3. 게시판 수정
4. 게시판 삭제
5. 

9.
"""


def input_number(max_number):
    num = input(f'1~{max_number}의 숫자를 입력하세요 : ')
    while not num.isdigit() or int(num) not in range(1, max_number + 1):
        print('잘못입력하셨습니다.')
        num = input(f'1~{max_number}의 숫자를 입력하세요 : ')
    return int(num)

def authenticate(id):
    pw = input('비밀번호 : ')
    idx = ids.index(id)
    real_pw = pws[idx]
    while pw != real_pw:
        print('비밀번호가 올바르지 않습니다.')
        pw = input('비밀번호 : ')
    return idx

# 주 실행문 구현
while run:
    print(mainMenu) # 메인메뉴 출력용
    if session is not None:
        print('로그인된 사용자 :', ids[session])

    select = input('>>>') # 사용자가 주메뉴선택 값을 select 넣는다.

    if select == '1':
        print('로그인(회원가입)메뉴로 진입합니다.')
        subRun = True
        while subRun: # 부메뉴 반복용
            print(memberMenu) # 회원관리 메뉴가 출력
            subSelect = input('>>> ') # 회원 부메뉴 선택값을 subSelect에 넣음
            if subSelect == '1':
                print('로그인 메뉴로 진입합니다.')
                id = input('아이디 : ')
                if id not in ids:
                    print('사용자가 존재하지 않습니다.')
                    continue
                session = authenticate(id)
                print('로그인이 되었습니다.')
                subRun = False
            elif subSelect == "2":
                print('회원가입 메뉴로 진입합니다.')
                id = input('아이디 : ')
                pw = input('비밀번호 :')
                pw_check = input('비밀번호 확인 :')
                if pw != pw_check:
                    print("비밀번호가 잘못 작성되었습니다.")
                    pw = input('비밀번호 :')
                    pw_check = input('비밀번호 확인 :')
                sns.append(len(sns) + 1)
                ids.append(id)
                pws.append(pw)
                group.append('normal')
                print('회원이 추가되었습니다.')
            elif subSelect == '3':
                print('회원 수정 메뉴로 진입합니다.')
                if group[session] == 'admin' or group[session] == 'professor':
                    print('회원 번호\t아이디\t비밀번호\t그룹')
                    for i in range(len(sns)):
                        print(f'{i + 1}\t{ids[i]}\t{pws[i]}\t{group[i]}\n')
                    num = input('수정할 회원 번호를 입력하세요 : ')
                    if not num.isdigit() or int(num) not in range(1, len(sns) + 1):
                        print('잘못 입력하셨습니다.')
                        num = input('수정할 회원 번호를 입력하세요 : ')
                    id = input('아이디 :')
                    pw = input('비밀번호 :')
                    ids[int(num)-1] = id
                    pws[int(num)-1] = pw
                    print('회원이 수정되었습니다.')
                elif group[session] == 'stu':
                    # 자신의 정보만 수정
                    print('본인의 계정만 수정 가능합니다.')
                    id = input('아이디 : ')
                    pw = input('비밀번호 : ')
                    ids[session] = id
                    pws[session] = pw
                    print('계정이 수정되었습니다.')
            elif subSelect == '4':
                print('회원 탈퇴 메뉴로 진입합니다.')
                if input('회원 탈퇴 하시겠습니까(y/n)? ') == 'y':
                    pw = input('비밀번호 : ')
                    real_pw = pws[session]
                    while pw != real_pw:
                        print('비밀번호가 올바르지 않습니다.')
                        pw = input('비밀번호 : ')
                    sns.pop(session)
                    ids.pop(session)
                    pws.pop(session)
                    group.pop(session)
                    print('회원 탈퇴가 완료되었습니다.')
                    subRun = False
                    session = None
                else:
                    print('회원 탈퇴가 취소되었습니다.')
            elif subSelect == '9':
                print('회원 관리 메뉴를 종료합니다.')
                subRun = False # 회원 while 종료
            else: # 1,2,3,4,9 말고 다른 키를 넣을 경우
                print('잘못된 메뉴를 선택하였습니다.')
    elif select == '2':
        print('성적관리 메뉴에 진입하였습니다.')
        # 성적관리
        if session is not None:
            if group[session] == 'professor':
                print('성적관리 메뉴에 진입하였습니다.')
                print('회원 번호\t아이디\t비밀번호\t그룹')
                for i in range(len(sns)):
                    print(f'{i + 1}\t{ids[i]}\t{pws[i]}\t{group[i]}')
                num = input('성적 입력할 학생의 번호를 입력해주세요 : ')
                while not num.isdigit() or int(num) not in range(1, len(sns) + 1):
                    print('잘못 입력하였습니다.')
                    num = input('성적 입력할 학생의 번호를 입력해주세요 : ')
                num = int(num)
                python = int(input('파이썬 점수 : '))
                database = int(input('데이터베이스 점수 : '))
                www = int(input('프론트엔드 점수 : '))
                total = python + database + www
                avg = total/3
                grade = None
                if avg >= 90:
                    grade = 'A'
                elif avg >= 80:
                    grade = 'B'
                elif avg >= 70:
                    grade = 'C'
                else:
                    grade = 'F'
                pythonScore.append(python)
                databaseScore.append(database)
                wwwScore.append(www)
                totalScore.append(total)
                avgScore.append(avg)
                gradeScore.append(grade)
                stuIdx.append(num - 1)
                print('성적이 입력되었습니다.')
            elif group[session] == 'stu':
                print('학생의 성적을 조회 합니다.')
                idx = stuIdx.index(session)
                if idx:
                    python = pythonScore[idx]
                    db = databaseScore[idx]
                    www = wwwScore[idx]
                    total = totalScore[idx]
                    avg = avgScore[idx]
                    grade = gradeScore[idx]
                    print(f'파이썬 : {python}, 데이터베이스 : {db}, 프론트엔드 : {www}')
                    print(f'총점 : {total}, 평균 : {avg}, 등급 : {grade}')
                else:
                    print('아직 성적이 입력되지 않았습니다.')
            else:
                print('권한이 존재하지 않습니다.')
        else:
            print('로그인을 해주세요.')
    elif select == '3':
        # 게시판
        print('게시판 메뉴에 진입하였습니다.')
        print('1. 게시글 생성')
        print('2. 게시글 목록 보기')
        print('3. 게시글 상세 보기')
        print('4. 게시글 수정')
        print('5. 게시글 삭제')
        print('9. 게시판 메뉴 나가기')
        num = input('번호를 입력해주세요 : ')
        if num == '1':
            title = input('제목 : ')
            content = input('내용 : ')
            no = len(board_no) + 1
            board_no.append(no)
            board_title.append(title)
            board_content.append(content)
            board_writer.append(session)
            print('게시글이 생성되었습니다.')
        elif num == '2':
            print('게시글 목록')
            for i in range(len(board_no)):
                print(f'No.{i + 1} / 작성자 : {ids[board_writer[i]]} / 제목 : {board_title[i]}')
        elif num == '3':
            print('게시글 상세 보기')
            print('게시글 내용을 볼 번호를 입력해주세요.')
            num2 = input_number(len(board_no)) - 1
            title = board_title[num2]
            content = board_content[num2]
            writer = ids[board_writer[num2]]
            print('제목 :', title)
            print('작성자 :', writer)
            print('내용 :', content)
        elif num == '4':
            print('게시글 수정')
            print('수정할 게시글 번호를 입력해주세요.')
            num2 = input_number(len(board_no)) - 1
            if board_writer[num2] == session:
                title = input('제목을 입력하세요 : ')
                content = input('내용을 입력하세요 : ')
                board_title[num2] = title
                board_content[num2] = content
                print('게시글이 수정되었습니다.')
            else:
                print('수정할 권한이 없습니다. 본인이 작성한 글만 수정 가능합니다.')
        elif num == '5':
            print('게시글 삭제')
            print('삭제할 게시글 번호를 입력해주세요.')
            num2 = input_number(len(board_no)) - 1
            if board_writer[num2] == session:
                board_no.pop(num2)
                board_title.pop(num2)
                board_content.pop(num2)
                board_writer.pop(num2)
                print('게시글이 삭제되었습니다.')
            else:
                print('삭제할 권한이 없습니다. 본인이 작성한 글만 삭제 가능합니다.')
        elif num == '9':
            print('게시판 메뉴를 나갑니다.')
            subRun = False
    elif select == '4':
        # 관리자 메뉴
        if session is not None:
            if group[session] == 'admin':
                print('관리자 메뉴에 진입하였습니다.')
                print('1. 회원 조회')
                print('2. 회원 등급 변경')
                print('3. 회원 삭제')
                num = input_number(3)
                if num == 1:
                    print('회원번호\t아이디\t비밀번호\t그룹')
                    for i in range(len(sns)):
                        print(f'{i + 1}\t{ids[i]}\t{pws[i]}\t{group[i]}')
                elif num == 2:
                    print('등급 변경할 회원 번호를 입력해주세요.')
                    num2 = input_number(len(sns)) - 1
                    print('1. 시스템담당자')
                    print('2. 교수')
                    print('3. 행정직원')
                    print('4. 학생')
                    print('5. 손님')
                    print('6. 학부모')
                    print('변경할 등급을 선택해주세요.')
                    num3 = input_number(6)
                    if num3 == 1:
                        group[num2] = "admin"
                    elif num3 == 2:
                        group[num2] = "professor"
                    elif num3 == 3:
                        group[num2] = "employee"
                    elif num3 == 4:
                        group[num2] = "stu"
                    elif num3 == 5:
                        group[num2] = "guest"
                    elif num3 == 6:
                        group[num2] = "parent"
                    print(f'{ids[num2]}님이 {group[num2]}으로 등급 변경되었습니다.')
                elif num == 3:
                    print('삭제할 회원 번호를 입력해주세요.')
                    num2 = input_number(len(sns)) - 1
                    sns.pop(num2)
                    id = ids.pop(num2)
                    pws.pop(num2)
                    group.pop(num2)
                    print(f'{id} 회원이 삭제되었습니다.')
            else:
                print('권한이 없습니다.')
        else:
            print('로그인을 해주세요.')
    elif select == '9':
        print('프로그램을 종료합니다.')
        run = False
    else:
        print('잘못 입력하셨습니다.')