from LMS.common import Session # 로그인한 member객체
from LMS.domain.Score import Score # 성적 객체

class ScoreService:
    @classmethod
    def load(cls): # 접속 테스트 용
        conn = Session.get_connection()
        # 세션객체에 있는 DB 연결 메서드를 실행하고 conn 변수에 넣음
        try:
            with conn.cursor() as cursor:
                # 커서 객체는 DB연결 성공 시 연결 정보를 가지고 있음
                cursor.execute('select count(*) as cnt from score')
                # SQL문 실행
                count = cursor.fetchone()['cnt']
                # 실행결과를 1개 가져와 count 변수에 넣음
                print(f"시스템 : 현재 등론된 성적 수는 {count}개 입니다.")

        except : print("ScoreService.load()메서드 실행오류 발생!")
            # 오류발생해도 시스템이 꺼지지 않음
        finally: conn.close() # DB 연결 정보를 닫는다.

    @classmethod
    def run(cls): # 성적처리용 주 메서드 실행용
        cls.load()
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member=Session.login_member # member 변수에 로그인 member의 상태를 가져옴
        if member.role in("manager","admin"): #매니저와 관리자에게만 보이는 메뉴창
            print("1. 학생성적 입력/수정")
        print("2. 내 성적조회") #모든 회원에게 보이는 메뉴창
        if member.role =="admin": #관리자에게만 보이는 메뉴창
            print("3. 전체 성적 현황(JOIN)")
        print("0.뒤로가기")
        sel = input(">>>")
        if sel == "1" and member.role in("manager","admin"): #1번을 입력하면 매니저와 관리자만 cls.add_score()로 이동
            cls.add_score()
        elif sel == "2": # 2번을 입력하면 ls.view_my_score()로 이동
            cls.view_my_score()
        elif sel == "3" and member.role =="admin": # 3번을 입력하면 관리자만 ls.view_all()로 이동
            cls.view_all()
        elif sel == "0":
            return

    @classmethod
    def add_score(cls): # 관리자와 매니저만 입력 가능
        target_uid = input("성적 입력할 학생 아이디 (UID): ").strip()
        conn = Session.get_connection()

        try:
            with conn.cursor() as cursor:
                # 1) 학생 조회
                # 부모테이블 자료가 있어야 자식 테이블에 자료를 넣는다.
                cursor.execute(
                    "SELECT id, name FROM members WHERE uid=%s",
                    (target_uid,)
                )
                student = cursor.fetchone() #members 테이블에 UID가 있으면 true /없으면 false

                if not student: # false일 때
                    print(f"{target_uid} 학생을 찾을 수 없습니다.")
                    return #객체가 있으면 아래 문 실행

                # 2) 점수 입력
                kor = int(input("국어점수: "))
                eng = int(input("영어점수: "))
                math = int(input("수학점수: "))

                # 3) Score 객체 생성( 여기 파이썬의 @property 계산됨)
                temp_score = Score(member_id=student["id"], kor=kor, eng=eng, math=math)

                # 4) 기존 성적 존재 여부 확인
                cursor.execute(
                    "SELECT 1 FROM scores WHERE member_id=%s",
                    (student["id"],)
                )
                exists = cursor.fetchone() is not None

                if exists:
                    # 5-A) UPDATE
                    sql = """
                    UPDATE scores
                    SET korean=%s,
                        english=%s,
                        math=%s,
                        total=%s,
                        average=%s,
                        grade=%s
                    WHERE member_id=%s
                    """
                    # 객체의 프로퍼티를 사용한다.(temp_score.total 등)
                    cursor.execute(sql, (
                        temp_score.kor,
                        temp_score.eng,
                        temp_score.math,
                        temp_score.total,
                        temp_score.avg,
                        temp_score.grade,
                        student["id"]
                    ))
                else: # 기존에 성적이 없으면 실행되는 문
                    # 5-B) INSERT 로직
                    sql = """
                    INSERT INTO scores
                        (member_id, korean, english, math, total, average, grade)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql, (
                        student["id"],
                        temp_score.kor,
                        temp_score.eng,
                        temp_score.math,
                        temp_score.total,
                        temp_score.avg,
                        temp_score.grade
                    ))

            conn.commit() # DB에 저장
            print(f"{student['name']}({student['id']}) 학생의 성적 저장 완료")

        finally:
            conn.close()


    @classmethod
    def view_my_score(cls):
        member=Session.login_member # 로그인한 member 객체
        conn = Session.get_connection() # DB 연결 객체
        try:
            with conn.cursor() as cursor: # 연결 성공 시 true
                # 로그인한 사람의 PK(ID)로 성적조회
                sql="SELECT * FROM scores WHERE member_id=%s"
                cursor.execute(sql, (member.id,))
                data = cursor.fetchone() # member의 DB 정보가 담김

                if data: # DB가 있으면
                    s = Score.from_db(data) # dict 타입의 객체를 s에 넣음
                    # 도메인 클래스의 __init__에서 uid 정보가 없으므로 세션 정보를 활용해 출력
                    cls.print_score(s, member.uid) # 콘솔에 보기 좋게 출력!!
                else:
                    print("등록된 성적이 없습니다.")
        finally:
            conn.close()

    @classmethod
    def print_score(cls, s, uid): # 개인 성적 출력과 전체 성적 출력도 가능한다
        # 도메인 모델(score)에 로직(@property)이 있으므로 s.total, s.avg 등을 그대로 사용
        print(
            f"ID : {uid:<10}|"
            f"국어 : {s.kor:>3} 영어 : {s.eng:>3} 수학 : {s.math:>3}|"
            f"총점: {s.total:>3} 평균 : {s.avg:>3} | 등급 :{s.grade:>3}"
        )

    @classmethod
    def view_all(cls):
        print("\n[전체 성적 목록 조회]")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql="""
                    SELECT m.uid, s.* \
                    FROM scores s \
                            JOIN members m ON s.member_id=m.id
                """
                cursor.execute(sql)
                datas = cursor.fetchall()
                for data in datas:
                    s = Score.from_db(data)
                    cls.print_score(s, data['uid'])

        finally:
            conn.close()



