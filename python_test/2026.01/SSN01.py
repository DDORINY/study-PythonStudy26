# 이름과 연락처 주민번호를 정보를 입력한다.
# 연락처가 정확히 입력이 되었는 지 확인 000-0000-0000 (12자리)
#                                 0123456789

print("{0:=^14}".format("※회원정보등록※"))

print("※성함을 입력해주세요!")
name = input(">>>")
print("※연락처를 입력해주세요! (예시 010-0000-0000)")
number = input(">>>")
ssn=""
if len(number) == 13:
    print("연락처 검토 중...")
else:
    print("잘못 입력되었습니다. 다시 실행해주세요.")
    exit(0)

if number[3] == "-"and number[8] == "-":
    print("연락처 검토 중...")
    print("확인되었습니다.")
else:
    print("잘못 입력되었습니다. 다시 실행해주세요.")
    exit(0)

print("※주민번호를 입력해주세요!")
ssn= input(">>>")
#주민번호 검증
if len(ssn) == 14:
    print("주민번호 검토 중...")
elif ssn[6] =="-":
    print("상적으로 등록되었습니다.")
else:
    print("잘못 입력되었습니다. 다시 실행해주세요.")
    exit(0)

print("="*15)
print("※입력된 성함 : " + name[0]+"*"+name[2])
print("※입력된 연락처 : " + number[0:3]+"****"+number[9:])
print("※입력된 주민번호 : " + ssn[0:8]+"******")

#생년월일 확인
print("{0:=^14}".format("※회원정보※"))
print("{0:<4}".format("이름")+"{0:>3}".format(":")+"{0:>6}".format(name))

year = ssn[0:2] #생년
month = ssn[2:4] #생월
day = ssn[4:6] #생일
sex = ssn[7] #성별
fullyear =""
if sex in ["1","2","5","6"]:
    fullyear = "19"+year
else:
    fullyear = "20"+year

print("{0:<4}".format("생년월일 :")+"{0:>6}".format(fullyear+"년생"))
#나이 계산
age = 2026-int(fullyear)
print("{0:<4}".format("나이")+"{0:>3}".format(":")+"{0:>7}".format(str(age)+"세"))

MW=""
if sex in ["1",",3","5","7"]:
    MW ="남성"
else:
    MW ="여성"
print("{0:<4}".format("성별")+"{0:>3}".format(":")+"{0:>6}".format(MW))

#출생지역
# 서울 00-08 부산 09-12 인천 13-15 경기16-25 강원26-34 충청 35-47 전라 48-66 경상 67-91 제주92-95
local =""
ssnlocal=ssn[8:10]

if int(ssnlocal) <9:
    local = "서울"
elif int(ssnlocal) <12:
    local = "부산"
elif int(ssnlocal) <15:
    local = "인천"
elif int(ssnlocal) <25:
    local = "경기"
elif int(ssnlocal) <34:
    local = "강원"
elif int(ssnlocal) <47:
    local = "충청"
elif int(ssnlocal) <66:
    local = "전라"
elif int(ssnlocal) <91:
    local = "경상"
else:
    local = "제주"
print("{0:<4}".format("출생지역 :")+"{0:>6}".format(local))
print()
print("""회원정보가 정상적으로 등록되었습니다. 
감사합니다.""")
print("="*15)