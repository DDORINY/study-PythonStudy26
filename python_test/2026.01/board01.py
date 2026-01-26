# 비회원용 게시판 만들기



# 프로젝트 목표
# c :게시글 등록
# r :게시글 전체보기(리스트)(제목)
# r :게시글 자세히 보기
# u :게시글 수정
# d :게시글 삭제

# 사용할 변수 리스트 (전역 변수 : 프로그램 전반적으로 사용가능한 변수)

run = True # while문 프로그램 구동중
board_no = [] # 중복되지않는 유일한 값,not null
board_title = [] # 게시글 제목
board_content = [] #게시글의 내용
board_writer = [] # 글쓴이
board_password = [] # 게시글의 암호(수정,삭제용)
board_hit = [] #추천
board_visitcount = [] # 조회수

# 주메뉴
menu = """
===============================
엠비씨 아카데미 비회원 게시판 입니다.

1. 게시글 등록
2. 게시글 리스트 보기
3. 게시글 자세히 보기
4. 게시글 수정하기
5. 게시글 삭제하기
6. 게시판 프로그램 종료

===============================
"""

# 프로그램 실행문
while run:
    print(menu)
    select = input("1~6 사이 입력하세요 >>> ")
    if select == "1":
        # select는 while 안에서만 활용되는 1회용 변수 (지역 변수)
        print(" 글작성 ")

        # 게시글의 번호는 프로세스가 자동처리
        # 키보드로 게시글을 받아 변수에 넣음
        title = input("제목 : ")
        content = input("내용 : ")
        writer = input("작성자 : ")
        password = input("암호 : ")
        # 넣은 정보 확인
        print(f"제목 {title}, 내용{content}")
        print(f"작성자 : {writer}, 암호 : {password}")
        choose = input("저장하려면 y를 누르세요. >>> ")
        if choose == "y":
            board_title.append(title)
            board_content.append(content)
            board_writer.append(writer)
            board_password.append(password)

            # 제목의 리스트에서 인덱스를 추출하여 +1인값이 no

            # 제목을 이용해서 번호를 생성하면 중복제목 문제 발생
            no = len(board_no) + 1

            board_no.append(no)
            board_hit.append(0) #추천
            board_visitcount.append(0) #조회수


            print(f"{no}번의 게시글이 등록되었습니다.")




    elif select == "2":
        print("[글 전체 보기]")

        print("----------------------------")
        print("번호\t 제목\t 작성자\t 조회수\t ")
        print("----------------------------")

        if len(board_no) == 0:
            print("등록된 글이 없습니다.")
            continue  # while 문으로 돌아간다

        for i in range(len(board_no)): #게시글의 갯수만큼 반복한다.
            print(f"{board_no[i]}\t {board_title[i]}\t {board_writer[i]}\t {board_visitcount[i]}")
            #          번호               제목              작성자                 조회수


    elif select == "3":
        print("[글 자세히 보기]")
        #idx = board_no.index(board_no[0])
        #board_no[idx] = int(input(f""
        bno = int(input("게시글 번호 >>"))

        if bno in board_no: # 등록된 게시물의 유무 확인
            print("등록된 글을 찾았습니다.")
            idx = board_no.index(bno) # 리스트에서 게시물의 인덱스 값을 찾아옴

            board_visitcount[idx] += 1
            print("------------------")
            print(f"번호 : {board_no[idx]}")
            print(f"제목 : {board_title[idx]}")
            print(f"내용 : {board_content[idx]}")
            print(f"작성자 : {board_writer[idx]}")
            print(f"조회수 : {board_visitcount[idx]}")
            print(f"추천 : {board_hit[idx]}")

            if input("추천 y : ") == "y":
                board_hit[idx] += 1
                print("추천 + 1")
            else:
                print("..")



        else:
            print("등록된 게시물이 없습니다.")




    elif select == "4":
        print(["글 수정"])
        bno = int(input("수정할 '글 번호' :  "))
        if bno in board_no:
            print("번호가 확인되었습니다.")
            idx = board_no.index(bno)
            print(f"제목 : {board_no[idx]}\n내용 : {board_content[idx]}")
            bpw = int(input("비밀번호"))
            if bpw in board_password:
                board_title[idx] = input(f"수정할 제목 : >>>")
                board_content[idx] = input(f"수정할 내용 : >>>")
                bpw2 = int(input("비밀번호"))







    elif select == "5":
        print(["글 삭제"])

    elif select == "6":
        print("종료")
        run = False

    else:
        print("잘못 입력하셧습니다.")
