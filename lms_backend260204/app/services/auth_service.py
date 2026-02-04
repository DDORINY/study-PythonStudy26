# ▶ 인증(Auth) 관련 서비스
# - 로그인 규칙 처리
# - 계정 활성 여부 확인
#
# 예외(ValueError)를 던지고
# Route에서 처리하게 설계

from app.repositories.member_repository import MemberRepository
#DB 접근용 로직을 만든 py파일을 불러온다.
class AuthService:
    @staticmethod
    def login(uid:str,pw:str)->dict :
        row = MemberRepository.find_by_uid_pw(uid,pw)
        if not row :
            raise ValueError("아이디 또는 비밀번호가 맞지 않습니다.")
            # print ("아이디 또는 비밀번호가 맞지 않습니다.") return<-이걸로 하지 않은 이유가 뭐지?
            # raise의 의미가 뭐지?/ValueError -> 오류 발생이 되어 이렇게 표시를 한건가?

        # 비활성화 계정인지 체크하기
        if not bool(row.get("active",True)):
        #기존에는 __str__작업을 했었지만 지금은 안해서 이렇게 코드가 변경된건가?
            raise ValueError("비활성화 계정입니다.")

        return row
