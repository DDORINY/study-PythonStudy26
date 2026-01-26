# 로그인/회원가입/내정보/정보수정/회원탈퇴/ 프로그램 종료

#메뉴창 구현
menu1 = """
===========
MBC 아카데미
===========
1. 로그인
2. 회원가입
3. 마이페이지
4. 관리자 페이지
5. 프로그램 종료
"""
submeun1 = """
===========
마이페이지
===========
1. 내정보
2. 내정보수정
3. 회원탈퇴
"""
submeun2 = """
===========
관리자 페이지 
===========
1.회원리스트
2.블랙리스트 설정
3.권한 설정
"""


#회원정보 리스트
nos = [1]
names = ["김도하"]
ids = ["kdh"]
passwords =["0606"]
numbers = ["010-5716-0160"]
ssns = ["930606-2181234"]
admins = [True]

#
no = nos[-1]+1
login_user = None
run = True

while run:
    print(menu1)
    select = input("1~3 숫자를 입력하세요: ")
    if select == "1":
        print("[로그인 페이지]")
        id=input("아이디 :")
        pw=input("암호:")
        if id in ids:
            idx=ids.index(id)
            if passwords[idx]==pw:
                login_user = idx
                print(f"[{names[idx]}로그인성공]")
            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("없는 아이디입니다.")


    elif select == "2":
        print("[회원가입 페이지]")
        print("사원번호 :"+str(no))
        id = input("아이디생성 :" )
        if id not in ids:
            print("아이디가 중복되지 않습니다.")
            pw = input("암호생성 :")
            name = input("이름 :")
            number = input("연락처 :")
            ssn = input("주민번호 :")
            admin = False
        else:
            print("아이디 중복")

        if input("회원가입 신청 (y:n) : ") =="y":
            nos.append(no)
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            numbers.append(number)
            ssns.append(ssn)
            admins.append(admin)
            print("회원가입이 완료되었습니다.")

    elif select == "3":
        if login_user is None:
            print("로그인 후 이용해주세요.")
            continue

        print(submeun1)
        choice = input("1~3 사이의 숫자를 입력하세요.")
        if choice == "1":
            print("[내정보]")
            print("이름 : "+names[login_user])
            print("연락처 :"+numbers[login_user])
            print("생년월일 :"+ssns[login_user][:6])


        elif choice == "2":
            print("[내정보수정]")

        elif choice == "3":
            print("[회원탈퇴]")
            pw1 =input("암호 확인 : ")
            if passwords[login_user] == pw1:
                nos.pop(login_user)
                ids.pop(login_user)
                passwords.pop(login_user)
                names.pop(login_user)
                numbers.pop(login_user)
                ssns.pop(login_user)
                admins.pop(login_user)
                print("탈퇴처리 되었습니다. ")
            else:
                print("비밀번호가 맞지 않습니다.")


    elif select == "4":
        if login_user is None:
            print("로그인 후 이용해주세요.")
            continue
        if login_user in admins == False:
            print(" 관리자 외 이용할 수 없는 페이지 입니다. ")
        else:
            print(submeun2)

    elif select == "5":
        print("[프로그램이 종료]")
        run = False

    else:
        print()