# ▶ 데이터베이스 연결 전용 모듈
# - pymysql을 이용해 DB connection 생성
# - DB 연결 로직을 한 곳에서 관리
#
# ✔ Repository에서만 사용
import pymysql
from app.config import Config # mysql로그인 정보 가져옴

def get_connection():
    return pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        db=Config.DB_NAME,
        charset='utf8mb4', #한국어 지원
        cursorclass=pymysql.cursors.DictCursor  # 딕셔너리상태로 가져옴
    )
