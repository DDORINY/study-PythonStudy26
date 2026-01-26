# 비회원용 게시판을 만들어보자

# C = 새글등록
# R = 리스트보기
# R = 자세히보기
# U = 게시글 수정
# D = 판매완료

# 사용할 변수 리스트 (전역변수 : 프로그램 전반적으로 사용할 변수)
run = True # while문 프로그램 구동 중!
board_no = [] # 중복되지 않는 유일한 값! not null
board_title = [] # 게시글 제목
board_content = [] # 게시글의 내용
board_writer = [] # 글쓴이
board_password = [] # 게시글의 암호 (수정, 삭제)
board_hit = [] # 좋아요!
board_visitcount = [] # 조회수!
board_message = []#댓글 변수

# 주메뉴
menu = """
⌈————————————————————————⌉
| MBC 아카데미 비회원 게시판 |
⌊————————————————————————⌋
[1] 게시글 등록
[2] 게시글 리스트보기
[3] 게시글 자세히보기
[4] 게시글 수정
[5] 게시글 삭제
[6] 프로그램종료
——————————————————————————"""



# 프로그램 실행문
while run:
    print(menu)
    #select는 while 문 안쪽에서만 활용되는 1회용 변수 : 지역변수
    select = input(">>>")
    if select == "1": # 입력된 값이 1이라면?
        print("———————[ 게시글 등록 ]———————")
        # 게시글 등록용 코드

        #게시물의 번호는 프로세스가 자동처리
        # 키보드로 게시글을 받아 변수에 넣음
        title = input("제목 | ")
        content = input("내용 | ")
        writer = input("글쓴이 | ")
        password = input("게시글 암호 | ")

        # 입력된 변수를 확인한다.
        sel=input(f"""———————[ 입력된 게시글 ]———————
제목 |{title}
내용 |{content}
글쓴이 |{writer}
암호 |{password}
게시글을 저장하시겠습니까? (y/n) """)
        if sel == "y":

            board_title.append(title)
            board_content.append(content)
            board_writer.append(writer)
            board_password.append(password)

            board_message.append([])
            # 제목의 리스트인덱스를 추출하여 +1한 값이 NO
            #for idx in range(len(board_title)):
            #    board_no.append(idx+1)

            no = len(board_no) + 1
            board_no.append(no)

            # 게시물의 좋아요 수를 0으로 값을 준다.
            board_hit.append(0)
            # 게시물의 조회 수를 0으로 값을 준다.
            board_visitcount.append(0)
            print(f"{no}번의 게시글이 등록되었습니다.")

        elif sel == "n":
            print("————————[ 게시글 취소 ]————————")
        else:
            print("입력된 값이 잘못되었습니다.")




    elif select == "2": # 입력된 값이 2이라면?
        print("—————[ 게시글 리스트보기 ]—————")
        # 게시글 리스트 보기용 코드 추가
        print("NO.\t 제목\t 작성자\t 조회수\t")

        if len(board_no) == 0:
            print("등록된 게시물이 없습니다.")
            continue

        for i in range(len(board_no)): #게시글의 개수만큼 반복
            print(f"{board_no[i]}\t {board_title[i]}\t {board_writer[i]}\t {board_visitcount[i]}")
            #          번호                제목                작성자                 조회수

    elif select == "3": # 입력된 값이 3이라면?
        print("—————[ 게시글 자세히보기 ]—————")
        # 게시글 자세히 보기 코드 추가
        bno = int(input("게시물 번호 조회 | "))

        if bno in board_no:
            idx = board_no.index(bno)
            board_visitcount[idx] += 1
            print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
            print(f"""NO. {board_no[idx]} 
제목 |{board_title[idx]}
내용 | {board_writer[idx]}
죄회수 | {board_visitcount[idx]}\t 좋아요 |{board_hit[idx]}""")

            if input("[좋아요] 누르기 (y/n) | ") =="y":
                board_hit[idx] += 1
                print(f"좋아요 {board_hit[idx]}")
            else:
                pass

            message = str(input("댓글 작성 | "))
            print(f"""————————————————————————————
NO. {board_no[idx]}       
제목 |{board_title[idx]}
내용 | {board_writer[idx]}
죄회수 | {board_visitcount[idx]}\t 좋아요 |{board_hit[idx]}""")

            if message :
                board_message[idx].append(message)
                print("\n[댓글 목록]")
                if len(board_message[idx]) == 0:
                    print("댓글이 없습니다.")
                else:
                    for i, msg in enumerate(board_message[idx], start=1):
                        print(f"{i}. {msg}")



            else:
                pass

        else:
            print("게시물이 없습니다.")


    elif select == "4": # 입력된 값이 4이라면?
        print("———————[ 게시글 수정 ]———————")
        # 게시글 수정 코드
        print("수정할 게시믈의 번호를 입력하세요!")
        bno = int(input("게시물 번호 조회 | "))
        if bno in board_no:
            idx = board_no.index(bno)
            print(f"""NO. {board_no[idx]} 
제목 |{board_title[idx]}
내용 | {board_writer[idx]}""")
            sel = input("암호를 입력해주세요) | ")
            if sel == board_password[idx]:
                board_title[idx] = input("제목변경 | ")
                board_content[idx] = input("내용변경 | ")
                print(f"""————————————————————————————
수정된 내용을 확인해주세요!
제목 |{board_title[idx]}
내용 |{board_content[idx]}
로 수정되었습니다.""")
            else:
                print("암호가 맞지않습니다.")
        else:
            print("없는 게시물입니다.")



    elif select == "5": # 입력된 값이 5이라면?
        print("———————[ 게시글 삭제 ]———————")
        # 게시글 삭제 코드
        bno = int(input("게시물 번호 조회 | "))
        if bno in board_no:
            idx = board_no.index(bno)
            print(f"""NO. {board_no[idx]} 
제목 |{board_title[idx]}
내용 | {board_writer[idx]}""")
            sel = input("삭제하시겠습니까? 암호를 입력해주세요) | ")
            if sel == board_password[idx]:
                board_no.pop(idx)
                board_title.pop(idx)
                board_content.pop(idx)
                board_visitcount.pop(idx)
                board_hit.pop(idx)
                board_password.pop(idx)
                board_writer.pop(idx)
                board_message.pop(idx)
                print("게시물이 삭제되었습니다.")


            else:
                print("암호가 맞지않습니다.")
        else:
            print("없는 게시물입니다.")

    elif select == "6": # 입력된 값이 6이라면?
        print("——————[ 프로그램 종료 ]——————")
        run = False

    else: # 입력된 값이 위의 값이 아니라면? 잘못입력된 값을 처리한다.
        pass