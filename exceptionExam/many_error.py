# 예외가 하나가 아닌 많은 에러가 발생할것 같을 때
# try문 안에서 여러개의 오류를 처리한다.

try :
    4 / 0
    a=[1,2]
    print(a[3])


# except ZeroDivisionError as e:
#     print(e)
#     print("0으로 나눠지는 예외가 발생함!!")
#
# except IndexError as e:
#     print(e)
#     print("리스트 인덱스 범위 초과")

except (ZeroDivisionError,IndexError) as e:
    print(e)
    print("0으로 나누거나 리스트의 범위초과 예외발생!")
    print("예외발생시 담당자에게 문의하세요!010-0000-0000")