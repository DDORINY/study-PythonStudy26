# 성적처리용 프로그램 개발

# C -> 성적입력 (과목 : 국어, 수학, 영어, 과학, 사회)
# R -> 성적보기 (과목별 점수,총점, 평균,등급)
# U -> 성적수정 (학번 검색 시 그 학번에 맞는 인덱스 값의 과목을 수정한다.-> 수정된 내용을 확인하고 저장버튼을 활성화 한다.)
# D -> 성적삭제

# 필요한 변수는?
sns = [] # 학번
names = [] # 이름(학생)
kors = [] # 국어점수
engs = [] # 영어점수
mats = [] # 수학점수
scis = [] # 과학점수
socs = [] # 사회점수
tots = [] # 빈 배열 총점
avgs = [] # 빈 배열 평균
grades = [] # 빈 배열 등급 (A,B,C,D,F 로 나눔)

menu ="""——————————————————
MBC 아카데미 성적처리 
——————————————————
[1] 성적입력
[2] 성적보기
[3] 성적수정
[4] 성적삭제
[5] 프로그램 종료
——————————————————"""

run = True # 프로그램 실행 중

while run: # run 변수가 False 처리될 때까지 반복
    # : 아래는 들여쓰기 4칸 정도처리
    # 들여쓰기를 진행하면 하위 실행문
    print(menu) # 콘솔창에 메뉴를 출력
    print("(1~5 값을 입력하세요.)")
    select = input(">>>") # select 변수에 숫자를 넣는다.
    #키보드로 입력받는 곳 앞쪽에 출력 메세지

    if select.strip() == "1": # 키보드로 입력한 숫자가 1인 경우
        # 학번으로 학생을 조회하고 성적을 입력할 수 있는 창을 구현한다.
        print("——————————————————\n[성적입력 페이지]")
        print("성적을 입력해주세요.\n——————————————————")
        sn = input("학번 : ")
        name = input("이름 : ")
        kor = int(input("국어 : "))
        eng = int(input("영어 : "))
        mat = int(input("수학 : "))
        sci = int(input("과학 : "))
        soc = int(input("사회 : "))# 키보드를 이용한 점수
        print("입력된 성적을 확인해주세요.\n——————————————————")
        print("학번 :"+sn )
        print("이름 :"+name )
        print(f"국어 : {kor}" )
        print(f"영어 : {eng}" )
        print(f"수학 : {mat}" )
        print(f"과학 : {sci}" )
        print(f"사회 : {soc}" )
        if input("Y/N : ").strip().lower() == "y":
            print(f"{name}학생의 성적이 입력되었습니다.")
            sns.append(sn)
            names.append(name)
            kors.append(kor)
            engs.append(eng)
            mats.append(mat)
            scis.append(sci)
            socs.append(soc) # 변수 뒤에 s는 배열 (리스트)라고 생각 #변수.append()리스트 뒤에 값이 추가됨
            tot=kor+eng+mat+sci+soc
            tots.append(tot)
            avg =tot/5
            avgs.append(avg)

            # 90 점 이상인 경우 A/ 80점 이상인 경우 B /70점 이상인 경우 C / 60점 이상인 경우 D/나머지 F
            if avg >= 90:
                grades.append("A")
            elif avg >= 80:
                grades.append("B")
            elif avg >= 70:
                grades.append("C")
            elif avg >= 60:
                grades.append("D")
            else:
                grades.append("E")



        elif input("Y/N : ").strip().lower() == "n":
            print("입력이 취소되었습니다.")

        else:
            print("잘못된 값이 입력되었습니다.\n 다시 처음부터 진행해주세요!")

    elif select.strip() == "2": # 키보드로 입력한 숫자가 2인 경우
        # 학번으로 학생을 조회하고 성적을 볼 수 있는 창을 구현한다.
        # 과목별 점수와 총점,평균, 등급도 확인되어야 한다.
        print("——————————————————\n[성적보기 페이지]\n——————————————————")
        print("[1] 전체 성적목록\n[2] 학생 성적 조회")
        choice = input(">>>")
        if choice == "1":
            for i in range (len(sns)): # 배열의 처음부터 끝까지 반복한다.
                # len(sns) -> 리스트의 길이를 가져온다.
                # range(5) 인경우 0~5까지 증가한다.
                # i in 5 -> i 값의 0반복,1반복 ,2반복 ,3반복, 4반복, 5까지


                print(f"""——————————————————
{i + 1}. {names[i]} 학생의 점수 ㅣ 학번 : {sns[i]} 
국어 : {kors[i]} 점 ㅣ 영어 : {engs[i]} 점
수학 : {mats[i]} 점 ㅣ 과학 : {scis[i]} 점
사회 : {socs[i]} 점 ㅣ 총점 : {tots[i]} 점
평균 : {avgs[i]} 점 ㅣ 등급 : {grades[i]} 등급 """)
        elif choice == "2":
            print("조회할 학생의 학번을 입력하세요.")
            sn = input("학번 :")
            if sn in sns:
                inx = sns.index(sn)
                print(f"""{names[inx]} 학생의 점수 ㅣ 학번 : {sns[inx]} 
국어 : {kors[inx]} 점 ㅣ 영어 : {engs[inx]} 점
수학 : {mats[inx]} 점 ㅣ 과학 : {scis[inx]} 점
사회 : {socs[inx]} 점 ㅣ 총점 : {tots[inx]} 점
평균 : {avgs[inx]} 점 ㅣ 등급 : {grades[inx]} 등급 """)
            else:
                print("잘못된 입력입니다.")


        else:
            print("잘못된 입력입니다.")


    elif select.strip() == "3": # 키보드로 입력한 숫자가 3인 경우
        # 학번으로 학생을 조회하고 성적을 수정할 수 있는 창을 구현한다.
        # 서브메뉴를 만들어 과목별 수정 창으로 이동 시킨다.
        print("——————————————————\n[성적수정 페이지]")
        print("수정할 학번을 입력해주세요.\n——————————————————")
        sn = input("학번 :")
        if sn in sns:
            inx = sns.index(sn)
            print(f"{names[inx]}의 성적을 수정해주세요.")
            kors[inx] = int(input(f"국어점수 :{kors[inx]} >>>"))
            engs[inx] = int(input(f"영어점수 :{engs[inx]} >>>"))
            mats[inx] = int(input(f"수학점수 :{mats[inx]} >>>"))
            scis[inx] = int(input(f"과학점수 :{scis[inx]} >>>"))
            socs[inx] = int(input(f"사회점수 :{socs[inx]} >>>"))
            tots[inx] = int(kors[inx]+engs[inx]+mats[inx]+scis[inx])
            avgs[inx] = int(tots[inx]) / 5

            if avgs[inx] >= 90:
                grades[inx] = "A"
            elif avgs[inx] >= 80:
                grades[inx] ="B"
            elif avgs[inx] >= 70:
                grades[inx] ="C"
            elif avgs[inx] >= 60:
                grades[inx] ="D"
            else:
                grades[inx] ="E"

            print(f"{names[inx]}의 성적이 수정되었습니다..")


    elif select.strip() == "4": # 키보드로 입력한 숫자가 4인 경우
        # 학번으로 학생과 과목을 조회하고 성적을 삭제하는 창을 구현한다.
        # 학번이 입력된 곳의 인덱스를 구하며 과목의 성적을 삭제처리한다.-값이 삭제되는 경우 다른 학번의 인덱스가 변경될 수 있으니 0값으로 처리?
        print("——————————————————\n[성적삭제 페이지]")
        print("삭제할 학번을 입력해주세요.\n——————————————————")
        sn = input("학번 :")
        if sn in sns:
            inx = sns.index(sn)

            sn_del = input(f"{names[inx]}의 성적을 삭제하시겠습니까? (y/n) :")
            if sn_del.strip().lower() == "y":
                sns.pop(inx)
                names.pop(inx)
                kors.pop(inx)
                engs.pop(inx)
                mats.pop(inx)
                scis.pop(inx)
                socs.pop(inx)
                tots.pop(inx)
                avgs.pop(inx)
                grades.pop(inx)

                print("삭제되었습니다. ")
            elif sn_del == "n":
                print("삭제 요청이 취소되었습니다.")
            else:
                print("잘못 입력되었습니다.")

    elif select.strip() == "5": # 키보드로 입력한 숫자가 5인 경우
        print("———————————————————\n[프로그램 종료]\n———————————————————")
        run = False # while문의 종료하여 프로그램이 꺼진다.

    else: # 1~5 이외의 값이 입력된 경우
        print("——————————————————\n잘못된 값을 입력하였습니다.\n다시 입력해주세요.")



