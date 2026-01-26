# 모듈 학습하기
# 모듈은 파이썬 파일로 만든 것을 연동하여 프로그램으로 처리
# 실무에서는 파일 1개로 모두 만들어 제공하는 것이 아니라
# 각각 기능이 있는 파일을 빼서 클래스화 하고 메서드로 동작한다.
# main.py ->__name__(__main__) 주 실행코드
# MemberService.py ->__name__(__MemberService__) 회원과리하는 클래스와 메서드
# ScoreService.py ->__name__(__ScoreService__) 성적관리하는 클래스와 메서드
# BoardService.py ->__name__(__BoardService__) 게시판을 관리하는 클래스와 메서드
# ItemService.py ->__name__(__ItemService__) 상품을 관리하는 클래스와 메서드
# CartService.py ->__name__(__CartService__) 장바구니를 관리하는 클래스돠 메서드

# python 확장자 .py로 만든 python파일은 모두 모듈로 처리 가능함

def add(a,d):
    return a+d

def sub(a,b):
    return a-b

# print(add(1,4))
# print(sub(4,2))

# 터미널에 python을 실행하고
# import mod1을 했던디
# 바로 print()문이 실행된다.
# 당연한 결과임 !
# 근데 main에서 실행하면??
# mod1.py에서 print 2개가 실행되고
# main.py에서 print 2개가 실행된다.
# main에서는 add와 sub 함수만 호출에서 사용하려고만 했다.
# 이때는 if문으로 실행을 조절해야한다.

if __name__ == '__main__':
    # 클래스나 모듈이 호출된 자신이 main 역할인지 확인
    print(add(3,4))
    print(sub(5,4))

print(__name__) # mod1
