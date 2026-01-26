# 상품에 대한 CRUD를 구현
# C ▶▶▶▶▶▶ 새상품 등록
# R ▶▶▶▶▶▶ 전체상품 목록
# R ▶▶▶▶▶▶ 단일상품 자세히 보기
# U ▶▶▶▶▶▶ 상품수정
# D ▶▶▶▶▶▶ 상품품절 / 상품삭제
from operator import index

#==========================
# ▶▶▶▶ [사용할 변수]
run = True
cate=""
import sys
# ▶▶▶▶ [상품 리스트]
item_names = ["노트북","모니터","꿀사과 1BOX","파이썬노트"] # 상품명
unit_prices = [1200000,400000,12000,10000] # 단가
quantity = [40,0,100,50] # 재고/수량
product_infor = ["Ai 삼성노트북","LG 24인치 LED","농부가 직접 재배한 꿀 사과","파이썬 자격증 한 번에 따자!"] # 상품정보
category = ["가전","가전","식품","도서"] # 상품분류 / 카테고리
sales = ["판매중","판매완료","판매중","판매중"] #판매상태
number_of_sales = [0,25,0,0] #누적 판매량
pays =["현금","카드"]

#==========================
# ▶▶▶▶ [사용할 메서드] /함수를 이용

def item_category():
    # 1. 카테고리 선택
    select = input("카테고리 선택 ▶")
    global cate
    if select == "1":
        cate = "패션의류/잡화"
    elif select == "2":
        cate = "뷰티"
    elif select == "3":
        cate = "식품"
    elif select == "4":
        cate = "생활용품"
    elif select == "5":
        cate = "가전"
    elif select == "6":
        cate = "오피스/사무"
    elif select == "7":
        cate = "도서"
    elif select == "8":
        cate = "헬스"
    elif select == "9":
        cate = "반려동물"
    elif select == "0":
        sys.exit()

    else:
        print("잘못입력되었습니다.")

    return cate



def new_item():
    item_category()
    print("new_item()함수 호출완료")
    print("▶▶▶▶ 상품등록 ◀◀◀◀")
    # 상품등록 추가용 실행문을 작성
    # 카테고리 설정을 한 상품의
    item_name = input("상품명 :")
    unit_price = int(input("판매가 :"))
    qua = int(input("재고수량 :"))
    infor = input("상품정보 :")
    save = input(f"""
==========================
등록하신 상품의 정보를 확인 후
상품을 등록해주세요. 
--------------------------
상품명 :{item_name}
판매가 :{unit_price}원
재고수량 :{qua}
상품정보 :{infor}
=========================
[1]저장
[2]취소
▶▶▶""").strip()
    if save == "1":
        print(f"{item_name}\n상품등록되었습니다.")
        item_names.append(item_name)
        unit_prices.append(unit_price)
        quantity.append(qua)
        number_of_sales.append(0)
        sales.append("판매중")
        category.append(cate)
        product_infor.append(infor)

    elif save == "2":
        print("상품등록이 취소되었습니다.")
    else:
        print("잘못입력되었습니다.\n다시입력해주세요.")


#====================================================
# 상품의 전체 리스트목록을 볼 수 있는 페이지
#====================================================
def item_list():
    print("item_list()함수 호출완료")
    print("=========================")
    print("▶▶▶▶ 상품목록 ◀◀◀◀")
    print("=========================")
    # 리스트 출력용 for item in item_names:
    print("NO|카테고리||상품명||가격|판매상태")

    for i in range(len(item_names)):
        print(f"{i + 1}.|{category[i]}|{item_names[i]}|{unit_prices[i]}원|[{sales[i]}]")



#====================================================
# 상품의 상세페이지 /카테고리별 상품을 볼 수 있게 해야한다.
#====================================================
def item_view():
    item_list()
    idx = int(input("상품번호 : "))
    idx -= 1

    # 인덱스 범위 체크 (핵심)
    if idx == 0 or idx > len(item_names):
        print("잘못 입력되었습니다.")
        return

    print(f"""
=========================
NO.{idx + 1} [{sales[idx]}]
카테고리 : {category[idx]}
상품명 :  {item_names[idx]}
단가 : {unit_prices[idx]}
판매수량 : {number_of_sales[idx]}
남은재고 : {quantity[idx]}
상품정보 : {product_infor[idx]}
=========================
""")
    order = input("[1] 상품구매 [2] 뒤로이동\n▶▶▶")
    if order == "1":
        if sales[idx]=="판매완료":
            print("판매가 완료된 상품입니다.")
            return

        print("=========================")
        print("상품구매페이지")
        print("=========================")
        sel = int(input("구매수량 :"))
        print(f"{item_names[idx]}을 {sel}개 \n총 금액은 {unit_prices[idx] * sel}원입니다.")
        sel2 = input("결제방식을 선택해주세요!\n[1]현금결제\n[2]카드결제\n▶▶▶")
        if sel2 == "1":
            sum = int(unit_prices[idx] * sel)
            pay = int(input(f"현금결제를 선택해주셨습니다.\n현금을 지불해주세요.\n▶▶▶"))
            if pay > sum:
                print(f"거스름돈 :{pay - sum}원")
                quantity[idx] -= sel
                number_of_sales[idx] += sel
                if quantity[idx] == "0":
                    sales[idx] = "판매완료"
            elif pay < sum:
                print("금액이 부족합니다.")
            elif pay == sum:
                print("결제가 완료되었습니다.")
                quantity[idx] -= sel
                number_of_sales[idx] += sel
                if quantity[idx] == 0:
                    sales[idx] = "판매완료"
            else:
                print("잘못입력되었습니다.")
        elif sel2 == "2":
            print("카드결제가 완료되었습니다.")
            quantity[idx] -= sel
            number_of_sales[idx] += sel
            if quantity[idx] == 0:
                sales[idx] = "판매완료"

    elif order == "2":
        return



#====================================================
# 상품수정페이지
#====================================================

def item_update():
    print("item_update()함수 호출완료")
    print("▶▶▶▶ 상품수정 ◀◀◀◀")
    # 상품정보를 수정하는 실행문을 작업
    item_list()
    idx = int(input("상품번호 :"))
    if 0 <= idx <= len(item_names):
        idx = idx - 1
        print(f"""
=========================
NO.{idx + 1} [{sales[idx]}]
카테고리 : {category[idx]}
상품명 :  {item_names[idx]}
단가 : {unit_prices[idx]}
판매수량 : {number_of_sales[idx]}
남은재고 : {quantity[idx]}
상품정보 : {product_infor[idx]}
=========================
""")
    modify = input("수정하실 목록을 선택해주세요.\n[1] 상품명\n[2] 단가\n[3] 수량 \n[4] 카테고리\n[5] 판매상태 \n▶▶▶")
    if modify == "1":
        print("상품명을 변경해주세요.")
        name =input("▶▶▶")
        item_names[idx] = name
        print(f"상품명이 변경되었습니다. ")
    elif modify == "2":
        print("상품 단가를 변경해주세요")
        prices = int(input("▶▶▶"))
        unit_prices[idx] = prices
        print(f"상품 단가가 변경되었습니다. ")
    elif modify == "3":
        print("상품 수량을 변경해주세요")
        qua = int(input("▶▶▶"))
        quantity[idx] = qua
        print(f"상품 수량이 변경되었습니다. ")
    elif modify == "4":
        print("상품의 카데고리를 변경해주세요.")
        item_category()
        category[idx] = cate
        print("상품의 카데고리가 변경되었습니다.")
    elif modify == "5":
        print("상품의 판매상태를 변경해주세요")
        sale = input("[1] 판매중\n[2]판매완료\n▶▶▶")
        if sale == "1":
            sales[idx] = "판매중"
            print("상품의 판매상태가 변경되었습니다.")
        elif sale == "2":
            sales[idx] = "판매완료"
            print("상품의 판매상태가 변경되었습니다.")
        else:
            pass



def item_delete():
    print("item_delete()함수 호출완료")
    print("▶▶▶▶ 상품삭제 ◀◀◀◀")
    # 상품의 판매상태를 변경하는 실행문을 작업
    item_list()
    idx = int(input("상품번호 :"))
    if 0 <= idx <= len(item_names):
        idx = idx - 1
        print(f"""
=========================
NO.{idx + 1} [{sales[idx]}]
카테고리 : {category[idx]}
상품명 :  {item_names[idx]}
단가 : {unit_prices[idx]}
판매수량 : {number_of_sales[idx]}
남은재고 : {quantity[idx]}
상품정보 : {product_infor[idx]}
=========================
""")
    delete =input("상품을 삭제하시겠습니까?\n[1] 삭제\n[2] 취소\n▶▶▶")
    if delete == "1":
        print("상품이 삭제되었습니다.")
        item_names.pop(idx)
        unit_prices.pop(idx)
        quantity.pop(idx)
        product_infor.pop(idx)
        category.pop(idx)
        sales.pop(idx)
        number_of_sales.pop(idx)
    elif delete == "2":
        print("상품삭제가 취소되었습니다.")

def main_menu():
    print("""
=================
  MBC 중고나라
=================
▶▶▶▶ 상품관리 ◀◀◀◀
[1] 상품등록
[2] 상품목록
[3] 상세페이지
[4] 상품수정
[5] 상품삭제
    
[0] 프로그램종료
=================
""")

def item_add_menu():
    print("""
=================
▶▶ 상품카테고리 ◀◀
_________________
[1] 패션의류/잡화
[2] 뷰티
[3] 식품
[4] 생활용품
[5] 가전
[6] 오피스/사무
[7] 도서
[8] 헬스
[9] 반려동물
[0] 프로그램 종료
=================
""")

#=========================
# 프로그램 주 실행 코드 시작!
while run:
    main_menu() # 메인메뉴 함수를 호출하여 출력
    select = input("바로 이동 ▶")
    if select == "1": # item_add_menu() 메뉴를 호출
        item_add_menu() # 아이템 추가용 메뉴 함수
        new_item()

    elif select == "2": # 전제 아이템 목록
        item_list()

    elif select == "3": # 아이템 상세페이지
        item_view()

    elif select == "4": # 아이템 수정
        item_update()
    elif select == "5": #아이템 판매상태변경
        item_delete()
    elif select == "0": #프로그램 종료
        run = False
    else:
        print("잘못입력되었습니다.\n 다시입력해주세요.")
