import os

class Attendance:
    def __init__(self,file_name="Attendance.txt"):
        self.file_name = file_name
        self.attendances = []
        self.session = None
        self.load_attendance()


    def load_attendance(self):
        self.attendances = []
        if not os.path.exists(self.file_name):
            self.save_attendance()
            return

        with open(self.file_name,'r',encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                data[0]=int(data[0])
                data[1]=int(data[1])
                data[2]=int(data[2])
                self.attendances.append(data)

    def save_attendance(self):
        with open(self.file_name,'w',encoding="utf-8") as f:
            for att in self.attendances:
                f.write(f"{att[0]}|{att[1]}|{att[2]}|{att[3]}\n")
                #           출석      지각      결석      UID


    def list_attendance(self):

        print("-"*300)
        print("NO.\tID\t출석\t지각\t결석")
        for i,att in enumerate(self.attendances):
            print(f"{i+1}\t{att[3]}\t{att[0]}\t{att[1]}\t{att[2]}")



    def attendance_add(self):

        print("-"*10)
        print("출석등록하실 학생의 아이디를 입력해주세요!")
        att_id=input(">>>")
        for att in self.attendances:
            if att[4] == att_id:
                att_no=input("""
    1. 출석
    2. 지각
    3. 결석
    >>>""")
                if att_no == "1":
                    att[0] = att[0]+1
                    print("출석등록완료")
                    self.save_attendance()
                    return

                elif att_no == "2":
                    att[1] = att[1]+1
                    print("지각등록완료")
                    self.save_attendance()
                    return

                elif att_no == "3":
                    att[2] = att[2]+1
                    print("결석등록완료")
                    self.save_attendance()
                    return

                else:
                    print("잘못등록되었습니다.")
                    return

        att_no = input("""
    1. 출석
    2. 지각
    3. 결석
    >>>""")
        if att_no =="1":
            self.attendances.append([1, 0, 0,att_id])
            print("출석등록완료")
            self.save_attendance()

        elif att_no =="2":
            self.attendances.append([0, 1, 0, att_id])
            print("지각등록완료")
            self.save_attendance()

        elif att_no =="3":
            self.attendances.append([0, 0, 1, att_id])
            print("결석등록완료")
            self.save_attendance()

        else:
            print("잘못입력되었습니다.")

    def modify_attendance(self):

        print("-" * 10)
        print("출석수정하실 학생의 아이디를 입력해주세요!")
        att_id = input(">>>")
        for i, att in enumerate(self.attendances):
            if att[3] == att_id:
                att_no=input("""
    -----------------------------------------
    1. 출석변경
    2. 지각변경
    3. 결석변경
    """)
                if att_no == "1":
                    print(f"현재등록된 출석 일:{att[0]}")
                    mod=int(input("수정하실 출석 일 : "))
                    print("-----------------------------------------")
                    print(f"출석일이 {att[0]}일에서 {mod}일로 변경되었습니다.")
                    att[0]= mod
                    self.save_attendance()

                elif att_no == "2":
                    print(f"현재등록된 지각 일:{att[1]}")
                    mod = int(input("수정하실 지각 일 : "))
                    print("-----------------------------------------")
                    print(f"지각일이 {att[1]}일에서 {mod}일로 변경되었습니다.")
                    att[1] = mod
                    self.save_attendance()

                elif att_no == "3":
                    print(f"현재등록된 결석 일:{att[2]}")
                    mod = int(input("수정하실 결석 일 : "))
                    print("-----------------------------------------")
                    print(f"결석일이 {att[2]}일에서 {mod}일로 변경되었습니다.")
                    att[2] = mod
                    self.save_attendance()

                else:
                    print("잘못입력되었습니다.")
            else:
                print("등록된 아이디가 없습니다.")

    def delete_attendance(self):

        print("-" * 10)
        print("출석삭제하실 학생의 아이디를 입력해주세요!")
        att_id = input(">>>")
        for i, att in enumerate(self.attendances):
            if att[3] == att_id:
                att_no = input(f"""
    -----------------------------------------
    {att[3]}학생의 정보를 모두 삭제하시겠습니까?
    1.삭제
    2.취소
    >>>""")
                if att_no == "1":
                    print("등록된 학생의 출석정보를 삭제되었습니다.")
                    self.attendances.pop(i)
                    self.save_attendance()

                elif att_no == "2":
                    print("등록되 학생의 출석정보 삭제가 취소되었습니다.")
                else:
                    print("잘못입력되었습니다.")


    def run(self):

        subrun = True

        if self.session is None:
            print("로그인 후 이용해주세요!")
            subrun = False
            return

        while subrun:
            print("""
    -----------------------------------------
      교수전용 출석관리 프로그램
    -----------------------------------------
    1. 출석 전체 조회
    2. 출석 등록
    3. 출석 수정
    4. 출석 삭제/취소
    -----------------------------------------
    0. 출석관리 종료
    """)
            subselect = input(">>>")
            if subselect == "1":
                print("[출석 전체 조회]")
                self.list_attendance()
            elif subselect == "2":
                print("[출석 등록]")
                self.attendance_add()
            elif subselect == "3":
                print("[출석 수정]")
                self.modify_attendance()
            elif subselect == "4":
                print("[출석 삭제/취소]")
                self.delete_attendance()
            elif subselect == "0":
                subrun = False
            else:
                print("잘못입력되었습니다.")
