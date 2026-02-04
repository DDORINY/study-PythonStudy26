# ▶ members 테이블 전용 DB 접근 로직 (SQL만)
# - 로그인용 조회
# - 회원 단건 조회
#
# 반환값: dict (row) 또는 None

from app.db import get_connection  #db.py에서 get_connection메서드를 가져옴
class MemberRepository: # MemberRepository 클래스 만들기

    """
    members 테이블에 대한 DB 접근만 담당하는 클래스
    - SQL만 작성
    - 비즈니스 로직 X
    """
#Repository 규칙 (이건 외워도 됨)

# ✔ Repository는:
# SQL만 쓴다
# dict 또는 None만 반환
# Flask 모른다
# session 모른다
# HTML 모른다
# ❌ 하면 안 되는 것:
# if 로그인 성공/실패 판단
# flash()
# redirect()

    @staticmethod  # 클래스에 묶여 있지만, 객체(self)나 클래스(cls)를 쓰지 않는 메서드
    # 이 메서드는 상태를 안쓰고, 그냥 기능만 제공한다.
    def find_by_uid_pw(uid :str, pw:str ):# 아이디와 페스워들르 찾는다 uid와 pw는 문자열이다.
        """
        아이디(uid)와 비밀번호(pw)로 회원 1명 조회 (로그인용)

        :param uid: 사용자 아이디 (문자열)
        :param pw: 비밀번호 (문자열)
        :return: dict(row) 또는 None
        """

        conn = get_connection()  # ->db에서 가져옴
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM members WHERE uid = %s AND password = %s"
                # members에서 uid와 pw가 맞는 것을 찾는다.
                cursor.execute(sql, (uid,pw))
                return cursor.fetchone() # dict이거나 None의 값을 갖는다.
        finally:
            conn.close()  #conn을 닫아준다.

    @staticmethod #클래스에 묶여 있지만, 객체(self)나 클래스(cls)를 쓰지 않는 메서드
    # 이 메서드는 상태를 안쓰고, 그냥 기능만 제공한다.
    def find_by_id(member_id:int): # member_id는 고유번호이다. 그래서 int 숫자열의 값을 갖는다.
        # 이 메서드는 member의 id를 찾는다.
        # 이걸 어디서 쓰는거지? 회원 단건 조회용인가? 맞음

        # member_id = session["member_id"]
        # member = MemberRepository.find_by_id(member_id)

        """
        회원 고유번호(id)로 회원 1명 조회

        :param member_id: members.id (PK)
        :return: dict(row) 또는 None
        """
        conn = get_connection()
        try :
            with conn.cursor() as cursor:
                sql = "SELECT * FROM members WHERE id = %s"
                cursor.execute(sql, (member_id,))
                return cursor.fetchone()
        finally:conn.cursor()