from LMS_260202.common.Session import Session
from LMS_260202.domain.Member import Member

class MemberService:

    @classmethod
    def load(cls):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT count(*) as cnt FROM members")
                count = cursor.fetchone()['cnt']
        finally: conn.close()

    @classmethod
    def login(cls):
        if Session.is_login():
            print("이미 로그인되어있습니다.")
            return

        print("[로그인]")
        uid = input("아이디 : ")
        pw =input("비밀번호 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM members WHERE uid = %s and password =%s"
                cursor.execute(sql, (uid, pw))
                row = cursor.fetchone()

                if row :
                    member =Member.from_db(row)
                    if not member.active:
                        print("비활성화된 계정입니다.")
                        return
                    Session.login(member)
                    print(f"{member.name}님 로그인 성공 ({member.role})")
                else :print("아이디 또는 비밀번호가 틀립니다.")
        finally: conn.close()

    @classmethod
    def logout(cls):
        if not Session.is_login() :
            print("현재 로그인 상태가 아닙니다.")
            return
        Session.logout()
        print("로그아웃되었습니다.")

    @classmethod
    def signup(cls):
        if Session.is_login():
            print("이미 로그인 상태입니다.")
            return
        uid = input("아이디 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT id FROM members WHERE uid = %s"
                cursor.execute(sql, (uid,))
                row = cursor.fetchone()
                if row :
                    print("중복된 아이디입니다.")
                    return

                pw = input("비밀번호 :")
                name = input("이름 : ")

                insert_sql ="INSERT INTO members (uid, password, name) VALUES (%s, %s, %s)"
                cursor.execute(insert_sql, (uid, pw, name))
                conn.commit()
                print("회원가입이 완료되었습니다.")
        except :
            conn.rollback()
        finally: conn.close()

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요!")
            return
        member=Session.login_member
        print(f"내정보 :{member}")
        print("""
  [1] 이름변경
  [2] 비밀번호 변경
  [3] 회원탈퇴 / 비활성계정
  [0] 뒤로가기""")
        sel = input(">>>")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if sel == "1":
                    print(f"변경하실 이름을 입력해주세요!")
                    new_name=str(input(">>>"))
                    if not new_name :
                        print("이름이 비어있습니다.")
                        return
                    sql = "UPDATE members SET name = %s WHERE id = %s"
                    cursor.execute(sql, (new_name, member.id))
                    conn.commit()
                    member.name = new_name
                    print("이름이 변경되었습니다.")
                elif sel == "2":
                    print(f"변경하실 비밀번호을 입력해주세요!")
                    new_pw =str(input(">>>"))
                    if not new_pw :
                        print("비밀번호가 입력되지 않았습니다.")
                        return
                    sql = "UPDATE members SET password = %s WHERE id = %s"
                    cursor.execute(sql, (new_pw, member.id))
                    conn.commit()
                    member.pw = new_pw
                    print("비밀번호가 변경되었습니다.")
                elif sel == "3":cls.delete()
                else :return
        finally: conn.close()


    @classmethod
    def delete(cls):
        if not Session.is_login():return
        member=Session.login_member
        print("회원탈퇴되었습니다.")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE members SET active = FALSE WHERE id = %s"
                cursor.execute(sql, (member.id,))
                conn.commit()
                Session.logout()
        finally: conn.close()
