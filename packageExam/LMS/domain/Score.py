# 성적관리 객체 만들기
# stu_uid,stu_name,subject,score,teacher,examination,u_day
class Score:
    def __init__(self,stu_uid,stu_name,subject,score,teacher,examination,u_day,active=True):
        self.stu_uid = stu_uid              # 등록된 학생의 아이디
        self.stu_name = stu_name            # 등록된 학생의 이름
        self.subject = subject              # 과목
        self.score = int(score)                  # 점수
        self.teacher = teacher              # 담당교수 -> 관리자 이름
        self.examination = examination      # 시험 -> 중간, 기말고사,과제 등
        self.u_day = u_day                  # 등록일
        self.active = active                # 공개, 비공개 여부

    def __str__(self):
        status = "활성" if self.active else "비활성"
        return f"{self.stu_uid}|{self.stu_name}|{self.subject}|{self.score}|{self.teacher}|{self.examination}|{self.u_day}|{status}"

    def to_line(self):
        return f"{self.stu_uid}|{self.stu_name}|{self.subject}|{self.score}|{self.teacher}|{self.examination}|{self.u_day}|{self.active}\n"

    @staticmethod
    def from_line(line:str):
        stu_uid,stu_name,subject,score,teacher,examination,u_day,active = line.strip().split("|")
        return Score(
            stu_uid = stu_uid,
            stu_name = stu_name,
            subject = subject,
            score = int(score),
            teacher = teacher,
            examination = examination,
            u_day = u_day,
            active = (active == "True"))
