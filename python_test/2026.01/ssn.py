# 주민번호를 입력 받아 생년월일 남녀 구분을 하는 코드
# input()함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 처리0 : 주민번호 입력 검증/1. 14글자인지 2.6번째에 -가 있는지
# 처리1 : 생년월일을 추출! ->1,2,5,6는 1900년생 나머지는 2000년생
# 처리2 : 주민번호 8번째 글자를 추출해서 성별구분
# 처리3 : 9-10번째 글자를 추출->출생지역
from calendar import month
print("="*15)
print("이름을 입력하세요!")
name = input(">>>")
print("="*15)

print("주민번호를 입력하세요!(-포함 14글자)")
ssn = input(">>>")

print("="*15)

# 입력된 주민번호 검증코드
if len(ssn) == 14: #키보드로 입력된 문자열이 14자인지 확인
    print("14자 입력이 확인되었습니다.")
else:
    print("!!주민번호 14자가 입력되지 않았습니다.!!")
    exit(0) #강제종료 됨!

if ssn[6] =="-":
    print("주민번호 7번째 구문자 인식완료되었습니다.")
else:
    print("!!주민번호 7번째 구문자가 입력되지 않았습니다.!!")
    print("!!프로그램을 처음부터 다시 실행하세요.!!")
    exit(0) #강제종료 됨!

print("-"*15)
print("입력된성함 : " + name)
print("입력된주민번호 : " + ssn)

#주민번호 앞 6자리를 생년월일로 추출 -> 1,2,5,6이면 1900년생/나머지는 2000년생
print("="*15)
year =ssn[0:2] #생년
month = ssn[2:4] #생월
day = ssn[4:6] #생일

fullyear = "" #if 안쪽에서 변수를 만들면 버그가 생길 수 있다. ""=null처리용
print("이름 :"+name)
if ssn[7] in ["1","2","5","6"] :
    fullyear = "19"+year
else :
    fullyear = "20"+year
print("생년월일 : "+fullyear+"년생")

# 나이를 계산해보자
age = 2026-int(fullyear)
print("나이 : "+str(age)+ "세") #print는 문자열+숫자열로 출력 오류 발생 -> 문자열로 변환(강제타입변환)->str(age)

# 주민번호 8번째 숫자가 1,3,5,7이면 남자~ 나머지는 여자!
gender =""
if ssn[7] in ["1","3","5","7"] :
    gender = "남성"
elif ssn[7] == "9" :
    gender = "외계인"
else :
    gender = "여성"
print("성별 : "+gender)

# 주민번호 9~10번째 숫자로 출생지역을 추출!
# 서울 00-08 부산 09-12 인천 13-15 경기16-25 강원26-34 충청 35-47 전라 48-66 경상 67-91 제주92-95
local = "" # 출생지를 판단하는 문자열
ssnlocal = ssn[8:10] #출생지 코드가 추출

if int(ssnlocal) <=8 :
    local = "서울"
elif int(ssnlocal) <=12 :
    local = "부산"
elif int(ssnlocal) <=15 :
    local = "인천"
elif int(ssnlocal) <=25 :
    local = "경기"
elif int(ssnlocal) <=34 :
    local = "강원"
elif int(ssnlocal) <=47 :
    local ="충청"
elif int(ssnlocal) <=66 :
    local = "전라"
elif int(ssnlocal) <=91 :
    local = "경상"
else:
    local = "제주"
print("출생지역 : "+local)
print("="*15)

