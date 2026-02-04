# DB 연결 코드 (기존 Session.py 대체/정리 버전)
# 기본 Session 클래스에서 사용했던 명령어
#  @staticmethod
#     def get_connection():
#           return pymysql.connect(
#             host="localhost",
#             user="mbc",
#             password="1234",
#             db="lms",
#             charset="utf8mb4",
#             cursorclass=pymysql.cursors.DictCursor
#             )
# ▶ 환경 설정 파일
# - SECRET_KEY (세션, 보안)
# - DB 접속 정보 (host, user, password, db)

# ✔ 나중에 개발/운영 환경 분리할 때도 여기서 관리

class Config:
    SECRET_KEY = "mbc-lms-secret"
    DB_HOST = "localhost"
    DB_USER = "mbc"
    DB_PASSWORD = "1234"
    DB_NAME = "lms"

# DB_HOST, SECRET_KEY 처럼 대문자로 쓰는 이유는
# ▶ “이건 설정값(상수)다” 라는 신호이자,
# ▶ Flask가 공식적으로 기대하는 규칙이기 때문이다.
#---------------------------------------------------
# Config 안의 값은 “바뀌면 안 되는 설정”이기 때문에 대문자,
# Flask는 대문자만 설정으로 인정한다.
