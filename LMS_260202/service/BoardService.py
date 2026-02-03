from LMS_260202.common.Session import Session
from LMS_260202.domain.Board import Board

class BoardService:
    @classmethod
    def run(cls):
        if not Session.is_login():
            print("로그인 후 이용가능합니다.")
            return

        while True:
            print("""
+--------------------------------------+
|         MBC 아카데미 LMS 게시판        |
+--------------------------------------+""")
            cls.list_board()
            print("""
            [1] 글쓰기
            [2] 글 상세보기 (수정/삭제가능)
            [0] 뒤로가기""")
            sel = input(">>>")
            if sel == "1":cls.write_board()
            elif sel == "2":cls.view_detail()
            elif sel == "0":break

    @classmethod
    def list_board(cls):
        print('-'*60)
        print(f"{'번호':>5}|{'제목':>5}|{'작성자':<10}|{'작성일'}")
        print('-'*60)
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                SELECT b.*, m.name
                FROM boards b
                JOIN members m ON b.member_id = m.id 
                ORDER BY m.id DESC
                """
                cursor.execute(sql)
                datas = cursor.fetchall()
                for data in datas:
                    date_str =data['created_at'].strftime("%Y-%m-%d")
                    print(f"{data['id']:<5}|{data['title']:<10}|{data['name']:<10}|{date_str}")
        finally:conn.close()

    @classmethod
    def write_board(cls):
        print("[새 글 작성]")
        title =input("제목 : ")
        content =input("내용 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO boards (member_id,title, content) VALUES (%s, %s,%s)"
                cursor.execute(sql, (Session.login_member.id, title, content))
                conn.commit()
                print("게시글이 작성되었습니다.")
        finally:conn.close()

    @classmethod
    def view_detail(cls):
        board_id = input("조회하실 글 번호 :")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                        SELECT b.*, m.name,m.uid
                        FROM boards b
                        JOIN members m ON b.member_id =m.id
                        WHERE b.id = %s
                        """
            cursor.execute(sql, (board_id,))
            row = cursor.fetchone()

            if not row:
                print("존재하지 않은 글 번호입니다.")
                return

            print("\n" + "*" * 40)
            print(f"제목 :{row['title']}")
            print(f"작성자 : {row['name']} ({row['uid']})")
            print(f"작성일 : {row['created_at']}")
            print("-" * 40)
            print(f"{row['content']}")
            print("*" * 40)

            if row['member_id'] == Session.login_member.id:
                print("1.수정   2.삭제   0.목록으로")
                sub_sel = input(">>>")
                if sub_sel == "1":
                    cls.update_board(board_id)
                elif sub_sel == "2":
                    cls.delete_board(board_id)
        finally:
            conn.close()

    @classmethod
    def update_board(cls, board_id):
        new_title = input("수정할 제목 : ")
        new_content = input("수정할 내용 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE boards SET title=%s, content=%s WHERE id=%s"
                cursor.execute(sql, (new_title, new_content, board_id))
                conn.commit()
                print("수정완료되었습니다.")
        finally:
            conn.close()

    @classmethod
    def delete_board(cls, board_id):
        confirm = input("삭제하시겠습니까?\n1.삭제 2. 취소")
        if confirm.lower() != "1": return

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "DELETE FROM boards WHERE id=%s"
                cursor.execute(sql, (board_id,))
                conn.commit()
                print("글이 삭제되었습니다.")
        finally:
            conn.close()