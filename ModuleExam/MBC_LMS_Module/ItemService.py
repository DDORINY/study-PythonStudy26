class ItemService:
    def __init__(self):
        items=[]
    def run(self):
        subrun4 =True
        while subrun4:
            print("""
    --------------------------
    1. 교재등록
    2. 교재조회
    3. 교재수정
    4. 교재삭제
    --------------------------
    0. 프로그램종료
    """)
            subrun4=input(">>>")
            if subrun4 == "1":
                print("[교재등록 서비스]")
            elif subrun4 == "2":
                print("[교재조회 서비스]")
            elif subrun4 == "3":
                print("[교재수정 서비스]")
            elif subrun4 == "4":
                print("[교재삭제 서비스]")
            elif subrun4 == "0":
                subrun4 = False
            else:
                print("잘못입력되었습니다.")