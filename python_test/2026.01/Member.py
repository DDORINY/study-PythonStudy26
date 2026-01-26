# 회원관리용 코드를 만든다.
# C -> 회원 추가
# R -> 관리자인 경우 (전체회원보기), 일반회원인 경우 (로그인)
# U -> 관리자인 경우 (회원관리(차단, 암호변경문의)), 일반회원인 경우 (내 정보 수정, 암호변경)
# D -> 회원 탈퇴

# 메뉴구현
run = True #프로그램 동작중을 관리하는 변수
login = True

# 사용할 리스트 변수를 생성한다.
sns = [1,2] # 사용자 관리번호
ids = ["kkw","lhj"] # 로그인용 id
passwords = ["1234","4321"] # 로그인용 pw
names = ["관리자","임효정"] # 사용자명
emails = ["admin@mbc.com","lhj@mbc.com"] # 이메일주소
admins = [True,False] # 관리자 유무 관리자:True /일반사용자 :False

sn = sns[-1] + 1
login_user= None


menu = """
===================================
     MBC 아카데미 회원관리 프로그램
===================================
 1. 회원가입
 2. 로그인
 3. 회원보기
 4. 내정보수정
 5. 프로그램종료
===================================
"""

while run:
    print(menu)
    select = input("1~5 숫자를 입력하세요: ")
    if select == "1":
        print("===================================")
        print("회원가입 메뉴에 진입하였습니다.")
        print("사원번호 :"+ str(sn))
        while login:
            id = input("아이디를 입력하세요. :")
            if id not in ids:
                pw = input("암호을 입력하세요. :")
                pw1 = input("암호 확인 : ")
                if pw == pw1:
                    print("비밀번호가 일치합니다.")
                elif pw != pw1:
                    print("비밀번호가 일치하지 않습니다.")
                    continue
                name = input("이름을 입력하세요. :")
                email = input("이메일주소를 입력하세요. :")
                admin = False
                login = False
            else:
                if id in ids:
                    print("아이디가 중복되었습니다. ")
                    print("아이디를 입력하세요.")
                else:
                    print("아이디를 입력하세요.")

        print("===================================")
        print("입력된 값을 확인하시고 Y를 누르세요.")
        print("이름 :"+name)
        print("아이디 :" + id)
        print("암호 :" + pw)
        print("이메일 :" + email )
        if input("Y/N : ").strip().lower() == "y":
            sns.append(int(sn))
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            emails.append(email)
            admins.append(admin)
            print("===================================")
            print("입력이 완료되었습니다.")

        else:
            print("===================================")
            print("처음부터 다시 진행하세요.")
            continue



    elif select == "2":
        print("===================================")
        print("로그인 화면에 진입하였습니다.")
        id = input("아이디 : ")
        pw = input("암호 : ")

        if id in ids :
            idx = ids.index(id)
            if passwords[idx] == pw:
                login_user = idx
                print(f"{names[idx]}로그인 성공")
                if admins[idx]:
                    print("▶ 관리자 계정입니다.")
                else:
                    print("▶ 일반회원 계정입니다.")
            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("아이디가 존재하지 않습니다.")


    elif select == "3":
        print("===================================")
        print("회원 정보 보기 메뉴에 진입하였습니다.")
        #관리자
        if login_user is None:
            print("로그인 후 이용 가능합니다.")
            continue

        if admins[login_user]:
            print("\n[전체 회원 목록]")
            for i in range(len(ids)):
                print(f"{i+1}. {names[i]}ㅣ{ids[i]}ㅣ{emails[i]}ㅣ관리자:{admins[i]} ")
        else:
            #일반회원
            print(f"\n{names[login_user]}님의 정보입니다.")
            print(F"아이디 :{ids[login_user]}")
            print(f"이메일 :{emails[login_user]}")



    elif select == "4":
        print("===================================")
        if login_user is None:
            print("로그인 후 이용 가능합니다.")
            continue

        print(f"\n{names[login_user]}님의 내 정보 수정 메뉴에 진입하였습니다.")
        print("""
1. 개명 신청
2. 이메일 변경
3. 암호 변경
4. 회원 탈퇴""")
        choice = input("1~3 숫자를 입력하세요: ")

        if choice == "1":
            names[login_user] = input("이름 개명신청 :")
            print("개명이 완료되었습니다."+names[login_user])
        elif choice == "2":
            emails[login_user] = input("이메일 변경 :")
            print("이메일변경 완료되었습니다."+emails[login_user])

        elif choice == "3":
            passwords[login_user] = input("암호 변경 :")
            print("암호가 변경 완료되었습니다."+passwords[login_user])

        elif choice == "4":
            sns.pop(login_user)
            names.pop(login_user)
            ids.pop(login_user)
            passwords.pop(login_user)
            emails.pop(login_user)
            admins.pop(login_user)
            login_user = None
            print("""회원탈퇴되었습니다. 이용해주셔서 감사합니다.""")

        else:
            print("잘 못된 입력입니다.")

    elif select == "5":
        print("회원가입 프로그램이 종료됩니다.")
        print("===================================")
        run = False

    else:
        print("1~5 숫자를 입력하세요!!")
