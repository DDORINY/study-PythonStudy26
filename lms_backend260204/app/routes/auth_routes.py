# ▶ 로그인 / 로그아웃 URL 담당
# - /login
# - /logout
#
# 세션(session)에 로그인 정보 저장/삭제
# URL ↔ Service 연결

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
# flask 기능 불러오기

from app.services.auth_service import AuthService
# Service class 불러오기

auth_bp = Blueprint("auth", __name__)
# "auth" Blueprint 이름 이 이름이 나중에 URL 식별자가 됨 예시)url_for("auth.login")
# __name__ :외울 필요 없음, 무조건 이렇게 씀

# URL들을 묶어주는 “미니 Flask 앱”왜 쓰냐?
# Flask 앱이 커지면 이런 문제가 생겨: app.py에 모든 URL 몰림
# 로그인 / 게시판 / 쇼핑몰 섞임
# 유지보수 지옥
# 그래서: 로그인 관련 URL → auth
# 메인 화면 → main
# 게시판 → board
# 처럼 기능 단위로 URL 묶기 위해 Blueprint를 씀

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    #이미 로그인 상태라면 홈으로 이동한다.
    if session.get("member_id"):
        return redirect(url_for("main.home")) # 여기서 main.home은 어디를 말하는 걸까?
                # redirect(url_for("main.home"))
                                    # main.home
                                    # │      └─ 함수 이름
                                    # └─ Blueprint 이름

    # app/routes/main_routes.py
    # main_bp = Blueprint("main", __name__)
    #
    # @main_bp.route("/")
    # def home():
    #     ...
    #그래서:
    # Blueprint 이름 → "main"
    # 함수 이름 → home
    # 👉 url_for("main.home") = /


    if request.method == "GET": # request.method 이건 어디서 나온거지? "GET", "POST"는 어디서 값을 부여받는거지?
        # request 는 뭐냐? from flask import request이다. 브라우저 요청 전체 정보/Flask가 자동으로 만들어줌
        # GET : 주소창 접속 / POST <form method="post"> 제출

        #member DB가 없다면 "login.html"로 이동하는 건가? X
        #그냥 로그인 화면 보여주는 단계 // DB 조회는 POST 요청에서만 한다.
        return render_template("login.html")
    uid = request.form.get("uid", "").strip()
    # html에서 form의 값을 받는건가? "" 이건 왜 들어갈까?
    # uid가 있으면 "uid",없으면 "" 값이다.
    pw = request.form.get("pw", "").strip()

    if not uid or not pw: # 아이디 또는 비밀번호 중 하나라도 비어 있으면
        flash("아이디와 비밀번호를 입력해주세요.") # flash() 1회성 메시지|다음 페이지에서 한 번만 보여짐
        return redirect(url_for("auth.login")) #새로고침 시 POST 재전송|브라우저 경고 뜸
    try:
        member =AuthService.login(uid,pw)
        session["member_id"] = member["id"]
        session["member_name"] = member.get("name","")
        flash(f"{member.get('name','')}님 로그인되었습니다.")
        return redirect(url_for("main.home"))
        #로그인 성공
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("auth.login"))

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("로그아웃 되었습니다.")
    return redirect(url_for("auth.login"))