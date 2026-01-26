#MBC 아카데미 회원프로그램 생성
#별도의 선생님들은 학생들의 성적을 전체보기 또는 수정 권한을 추가한다.


menu1 ="""
———————————————————
MBC 아카데미 프로그램
———————————————————
[1] 로그인
[2] 회원가입
[3] 프로그램종료
"""

menu2 ="""
————————————————————————
MBC 아카데미 학생관리프로그램
————————————————————————
•선생님 계정입니다.•
[1] 수업생성
[2] 수업조회ㅣ수정
[3] 수업삭제
[4] 학생정보조회ㅣ수정 
[5] 성적정보등록
[6] 성적정보조회ㅣ수정
[7] 로그아웃
"""

menu3 ="""
——————————————————————
MBC 아카데미 학생프로그램
——————————————————————
[1] 마이페이지ㅣ내정보수정
[2] 수업신청ㅣ신청수업조회
[3] 시험성적표
[4] 로그아웃
"""
# 로그인 상태
login_user = None

# 로그인 및 회원가입 리스트 데이터

sns=["320-00"]
pws=["1234"]
names=["김도하"]
numbers=["010-1234-1234"]

# 신청과목 and 학생 수업신청여부 리스트
clas =["국어","수학","영어"]
cours = [["True","True","True"]]

# 학생, 선생님 구분
users =["T"] #T=선생 S=학생



#menu1 페이지 구현
run = True
while run:
    print(menu1)
    select = input("페이지 이동 ▶")
    if select == "1":

        print("[로그인 페이지]\n——————————")
        sn = input("학번/사번 : ").strip()
        if sn in sns:
            inx = sns.index(sn)
            pw = input("암호 : ").strip()
            if pw == pws[inx]:
                print("[로그인성공]")
                login_user = inx
                # menu2페이지 구형 #•선생님 계정입니다.•
                while users[inx] == "T":
                    print(menu2)
                    sel2 =input("페이지 이동 ▶")
                    if sel2 == "1": #[1] 수업생성
                        print("[수업생성 페이지]")
                        cla = input(f"생성할 수업 명 ▶ ").strip()
                        new =input("수업을 생성하시겠습니까? (y/n) ▶ ")
                        if new =="y":
                            if cla in clas:
                                print("중복된 과목입니다.")
                            else:
                                clas.append(cla)
                                #자동으로 수업 미등록 2차원 리스트에 추가해야함
                                i = 0
                                while i < len(cours):
                                    cours[i].append("False")
                                    i += 1
                                    print(f"[과목 추가 완료] 현재 과목: {clas}")


                        else:
                            print("수업 생성이 취소되었습니다.")

                    elif sel2 == "2": #[2] 수업조회ㅣ수정
                        print("[수업조회&수정 페이지]")

                    elif sel2 == "3": #[3] 수업삭제
                        print("[수업삭제 페이지]")

                    elif sel2 == "4": #[2] 학생정보조회ㅣ수정
                        print("[학생정보&수정 페이지]")

                    elif sel2 == "5": #[3] 성적정보등록
                        print("[성적정보등록 페이지]")

                    elif sel2 == "6": #[6] 성적정보조회ㅣ수정
                        print("[성적정보조회&수정 페이지]")

                    elif sel2 == "7": #[7] 로그아웃
                        print("로그아웃되었습니다.")
                        login_user = None
                        break



                else:
                    print(menu3)
                    # menu3페이지 구형 #•선생님 계정입니다.•
                    sel3 = input("페이지 이동 ▶ ")
                    while users[inx] == "S":
                        if sel3 == "1": #마이페이지ㅣ내정보수정
                            print("[마이페이지]")
                            print(f"""{names[inx]}님 환영합니다.
학번 :{sns[inx]}ㅣ연락처 :{numbers[inx]}""")
                            sel4 = input("정보수정(y/n) ▶ ")
                            if sel4 == "y":
                                numbers[inx] = input("연락처 ▶ ").strip()
                            else:
                                print("정보수정취소")


                        elif sel3 == "2": #수업신청ㅣ신청수업조회
                            print("[수업신청&조회 페이지]")
                            print(f"{names[inx]}님의 수업신청 목록")
                            if "True" not in cours[inx]:
                                print("신청한 수업이 없습니다.")
                            else:
                                for i in range(len(cours)):
                                    print(f"{i + 1}. {cours[inx][i]}")
                                else:
                                    print("신청한 수업이 없습니다.")

                            #수업신청
                            sel4 = input("수업을 신청하실건가요?(y/n) ▶ ")
                            if sel4 == "y":
                                cla = input("신청과목 ▶ ").strip()

                                #신청하는 과목과 과목리스트가 맞는 지 확인하고 인덱스로 값을 변경해준다.
                                if cla in clas:
                                    print("정상적으로 등록되었습니다.")
                                    inxx=clas.insert(inx, cla)



                            elif sel4 == "n":
                                break
                            else:
                                break

                        elif sel3 == "3":#시험성적표
                            print("[시험성적표 페이지]")

                        elif sel3 == "4": #로그아웃
                            print("로그아웃되었습니다.")
                            login_user = None
                            break


            else:
                print("[비밀번호 불일치]")

        else:
            print("미등록 학번")




    elif select == "2":
        print("[회원가입 페이지]\n——————————")
        sn = input("학번/사번(예시:320-01) ▶ ")
        if sn not in sns:
            pw = input("암호 ▶ ")
            name = input("이름 ▶ ")
            number = input("연락처 ▶ ")
            choice1 = input(f"저장하시겠습니까? (y/n) ▶ ")

            user = "S" #기본값은 학생으로 등록된다.

            if choice1 == "y":
                sns.append(sn)
                pws.append(pw)
                names.append(name)
                numbers.append(number)
                users.append(user)
                #수업신청 2차 리스트를 "False"로 과목 리스트번 등록한다.
                cours.append(["False"] * len(clas))

            elif choice1 == "n":
                print("[회원가입취소]")
            else:
                print("[입력오류]")
        else:
            print("중복된 학번/사번입니다.")



    elif select == "3":
        print("프로그램 종료\n——————————")
        run = False
    else:
        print("잘못 입력되었습니다.\n——————————")


