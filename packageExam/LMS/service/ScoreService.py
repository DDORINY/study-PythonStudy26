import os
from packageExam.LMS.domain import *
from packageExam.LMS.common import Session
from packageExam.LMS.service.MemberService import MemberService
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "..","data","score.txt")
class ScoreService:
    scores = []

#############################
# 파일 불러오기 저장하기#
#############################
    @classmethod
    def load(cls):
        cls.scores = []
        if not os.path.exists(FILE_NAME):
            cls.save()
            return

        with open(FILE_NAME,"r",encoding="utf-8") as f:
            for line in f:
                cls.scores.append(Score.from_line(line))

    @classmethod
    def save(cls):
        with open(FILE_NAME,"w",encoding="utf-8") as f:
            for score in cls.scores:
                f.write(score.to_line())

#############################
    # 성적관리 서비스 def #
#############################
    @classmethod
    def list_score(cls):
        if Session.login_member is None:
            print("로그인 후 이용가능합니다.")
            return
        member = Session.login_member
        print("""
    -------------------------------
            MBC 아카데미 내성적    
    -------------------------------""")
        for score in cls.scores:
            if score.stu_uid == member.uid:
                print(f"""
    과목 :{score.subject} 점수 : {score.score}""")
        print(f"""
    {member.name}의 성적입니다.""")

    @classmethod
    def score_add(cls):
        member = Session.login_member
        if member.role == "admin":
            print(f"""
    -------------------------------
           MBC 아카데미 성적등록    
    -------------------------------
            """)
            teacher_name = member.name
            stu_uid = input("학생의 아이디 :")
            stu_name = None
            for m in MemberService.members:
                if m.uid == stu_uid:
                    stu_name = m.name
                    print(f"{m.name}학생의 성적등록해주세요!")
                    stu_name=m.name
                    subject = input("과목 :")
                    score = int(input("점수 :"))
                    examination =input("시험종류 :")
                    now=datetime.now().strftime('%x')
                    score_info = Score(
                        stu_uid=stu_uid,
                        stu_name=stu_name,
                        subject=subject,
                        score=score,
                        examination=examination,
                        teacher=teacher_name,
                        u_day=now,
                        active =True)

                    cls.scores.append(score_info)
                    cls.save()
                    print(f"{stu_name}학생 성적이등록되었습니다.")
                    return

        else:print("관리자로 로그인해주새요!")


    @classmethod
    def score_modify(cls):
        member = Session.login_member
        if member.role == "admin":
            print(f"""
    -------------------------------
          MBC 아카데미 성적수정    
    -------------------------------""")
            for i,score in enumerate(cls.scores):
                print(f"[{score.examination}]이름:{score.stu_name}| 과목:{score.subject}| 점수:{score.score}\n담당교수:{score.teacher} 등록일자:{score.u_day}")
                print("-------------------------------")


    @classmethod
    def score_delete(cls):
        print(f"""
    -------------------------------
           MBC 아카데미 성적삭제    
    -------------------------------
            """)
