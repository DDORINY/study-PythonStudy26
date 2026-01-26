class ScoreService:
    def __init__(self, member_service):
        self.ms = member_service          # Member_service의 객체를 받아서 보관하겠다.




        # 성적 데이터 ( 리스트로 만들기 )
        # s[0]=학생ID, s[1]=이름, s[2]=국어, s[3]=영어, s[4]=수학
        self.scores = [["kdg", "김도균", 85, 90, 80]]       # 성적을 담을 리스트값 생성 및 표본 리스트 넣기



#===========================================
# 점수를 등급으로 변환하는 계산 메서드 추가
#===========================================
    def grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

#============================================
# 점수관리 프로그램에서 사용할 학생/교수/관리자의 공통 메서드 묶음 ( 전체 성적 보기 )
#============================================
    def all_scores(self):
        for s in self.scores:
            avg = (s[2] + s[3] + s[4]) / 3
            print(f"{s[1]} | 국어 {s[2]} | 영어 {s[3]}| 수학 {s[4]} | 평균 {avg:.2f} | 등급 {self.grade(avg)}")



#============================================
# 학생 전용 메서드 묶음 ( 나의 점수 보기 )
#============================================
    def my_score(self):
        if self.ms.session is None:
            print("로그인 후 이용 가능합니다.")
            return

        idx = self.ms.session
        role = self.ms.roles[idx]

        if role != "student":
            print("이것은 학생 전용 기능입니다!")

        my_id = self.ms.session[idx]

        for s in self.scores:
            if s[0] == my_id:
                avg = (s[2] + s[3] + s[4]) / 3

                print(f"""
이름: {s[1]}
국어: {s[2]}
영어: {s[3]}
수학: {s[4]}
평균: {avg:.2f}
등급: {self.grade(avg)}
""")
                return

        print("성적 정보가 없습니다.")




#============================================
# 해당 프로그램에서 교수 / 관리자의 고유 메서드 묶음
#============================================

#===============================================
# 학생 성적 입력 ( 교수 / 관리자 고유의 권한 )
#===============================================
    def insert_score(self):
        idx = self.ms.session
        role = self.ms.roles[idx]

        if role in ["professor", "admin"]:
            print("교수, 관리자 전용 페이지입니다. ")
            return


        sid = input("학생 ID >> ")
        name = input("이름 >> ")
        kor = int(input("국어 >> "))
        eng = int(input("영어 >> "))
        math = int(input("수학 >> "))

        self.scores.append([sid, name, kor, eng, math])            # 입력된 정보를 scores에 담는다.
        print("성적 입력 완료")

#==============================================
# 학생 성적 수정 ( 교수 / 관리자 고유의 권한 )
#==============================================
    def update_score(self):
        idx = self.ms.session
        role = self.ms.roles[idx]

        if role not in ["professor", "admin"]:
            print("교수, 관리자 전용 페이지입니다. ")


        sid = input("학생 ID를 입력하세요 : ")

        for s in self.scores:
            if s[0] == sid:
                s[2] = int(input("국어 : "))
                s[3] = int(input("영어 : "))
                s[4] = int(input("수학 : "))
                print("성적 수정 완료")
                return

        print("해당 학생이 없습니다.")

# ==============================================
# 학생 성적 삭제 ( 교수 / 관리자 고유의 권한 )
# ==============================================

    def delete_score(self):
        idx = self.ms.session
        role = self.ms.roles[idx]

        if role != "admin":
            print("관리자 전용 기능입니다.")
            return

        sid = input("삭제할 학생 ID >> ")

        for s in self.scores:
            if s[0] == sid:
                self.scores.remove(s)
                print("성적 삭제 완료")
                return

        print("해당 학생이 없습니다.")



#==============================================
#  프로그램 구동부  ( 메뉴 등 )
#==============================================
    def run(self):
        if self.ms.session is None:                         # 불러온 Membersession 에서 로그인 상태가 아닐 경우!
            print("로그인 후 이용 가능합니다.")
            return

        run = True                                          # 아까 실행 에러났던 부분 참조해서 run값 함수안에 넣기
        while run:
            print("""
==============================
엠비씨 아카데미 LMS 성적관리 페이지
==============================
1. 나의 성적 보기 (학생)
2. 전체 성적 보기 (공용)
3. 학생 성적 입력 (교수/관리자)
4. 학생 성적 수정 (교수/관리자)
5. 학생 성적 삭제 (관리자)
9. 성적관리 페이지 나가기
""")

            select = input("선택 >> ")

            if select == "1":
                self.my_score()
            elif select == "2":
                self.all_scores()
            elif select == "3":
                self.insert_score()
            elif select == "4":
                self.update_score()
            elif select == "5":
                self.delete_score()
            elif select == "9":
                run = False
            else:
                print("잘못된 선택입니다.")