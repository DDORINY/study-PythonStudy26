# ▶ 메인 페이지 담당
# - /
# - 로그인 여부 체크
#
# 로그인 안 되어 있으면 /login으로 redirect

from flask import Blueprint, render_template, session, redirect, url_for

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    # 로그인 안했다면 로그인으로
    if not session.get("member_id"):
        return redirect(url_for("auth.login"))
    return render_template("home.html",name=session.get("member_name",""))