# 자판기 프로그램 만들기

#필요한 리스트
product_no = [1,2,3,4,5,6] # 판매상품 번호
product_menu = ["초콜릿", "사탕","젤리","견과류", "빵", "컵라면"] #상품리스트
selling_price = [1000,500,2000,2500,1500,1900] #상품판매가
inventory_quantity = [10,10,10,10,0,10]
sales_status = ["판매중","판매중","판매중","판매중","품절","판매중"] #판매상태
sellers1 = ["0000"] #관리자 코드는 초기 0000으로 셋팅 / 판매자코드 등록 후 이용이 가능
sellers = ["1234"]
payments = ["현금","카드"] #결제 방식
details_s =[0,0,0,0,0,0]

#회원가입 변수#

sns = [1,] #판매담당자 번호
ids = ["kdh"]  #판매담당자 아이디
pws = ["1234"] #판매담당자 암호
names = ["김도하"] #담당자 이름
numbers = ["010-5716-0160"] #담당자 연락처

run = True
subrun = True
subrun2 = True
login_user =None

#상품리스트의 메뉴판을 만들자!
main = """
=========================
자판기 프로그램 
=========================
[1] 상품리스트
[2] 판매자 페이지
[3] 프로그램종료"""

menu = """
=========================
판매자 페이지
=========================
[1] 로그인
[2] 회원가입
[3] 대시보드
[4] 상품등록
[5] 상품관리
[6] 로그아웃
[7] 뒤로가기
[8] 프로그램 종료"""

submenu = """
=========================
상품수정 페이지
=========================
[1] 상품수정
[2] 입출고관리
[3] 판매상태변경
[4] 상품삭제
[5] 로그아웃
[6] 뒤로가기
[7] 프로그램 종료"""


while run:
#####################################################################################################
#메인메뉴#
    print(main)
    sel = input(">>>")
    #=========================
    #자판기 프로그램
    #=========================
    #[1] 상품리스트
    #[2] 판매자 페이지
    #[3] 프로그램종료
    if sel == "1":
        print("=========================")
        print("상품 리스트")
        print("=========================")
        if sales_status == "품절":
            print("상품 준비 중 입니다.")

        for i in range(len(product_no)):
            print(f"상품번호 {product_no[i]}.상품명:{product_menu[i]} | 금액:{selling_price[i]}원 | {sales_status[i]}")

        print("_________________________")
        pur_no = int(input("구매하실 상품번호을 입력해주세요.\n>>>"))
        if pur_no in product_no:
            idx = product_no.index(pur_no)
            if sales_status[idx] =="품절":
                print("재고가 없습니다. 다시 선택해주세요.")
            elif sales_status[idx] =="판매중":
                print(f"{product_menu[idx]}상품의 결제 금액은 {selling_price[idx]}원입니다.")
                print("_________________________")
                pay = input("결제하실 지불방법을 선택해주세요. \n[1] 현금결제\n[2] 카드결제\n>>>")
                if pay == "1":
                    pay2 = int(input("입금금액을 입력해주세요 \n>>>"))
                    print("_________________________")
                    if pay2 > selling_price[idx]:
                        print(f"거스름돈은 {pay2-selling_price[idx]}원입니다.")
                        print("_________________________")
                        inventory_quantity[idx] -=  1
                        details_s[idx] += 1
                        if inventory_quantity[idx] == 0:
                            sales_status[idx] = "품절"
                        else:
                            pass

                    elif pay2 < selling_price[idx]:
                        print("금액이 부족합니다.")
                    elif pay2 == selling_price[idx]:
                        print("결제되었습니다.")
                        details_s[idx] += 1
                        inventory_quantity[idx] -= 1
                        if inventory_quantity[idx] == 0:
                            sales_status[idx] = "품절"
                        else:
                            pass

                elif pay == "2":
                    print("카드결제되었습니다. ")
                    inventory_quantity[idx] -=1
                    details_s[idx] += 1
                    if inventory_quantity[idx] == 0:
                        sales_status[idx] = "품절"
                    print("_________________________")
                else:
                    print("잘못입력되었습니다.")
            else:
                pass
        else:
            print("없는 상품입니다.")

#####################################################################################################
#판매자 코드 등록#
    elif sel == "2":
        seller = input("판매자 코드를 입력해주세요.\n>>>") #판매자 변수= seller / 판매자코드리스트 = sellers
            #판매자 코드는 초기 셋팅을 잡고 사용할 수 있도록 설정할 예정이다.관리자 코드는 0000
        if seller in sellers1:
            print("관리자님 안녕하세요.\n 판매자코드를 등록해주세요.")
            seller2 = input(">>>")
            seller3 =input(f"판매자 코드는 {seller2}로 등록하시겠습니까? (y/n)\n>>>")
            if seller3 == "y":
                print("정상적으로 등록되었습니다.")
                sellers.append(seller2)
            elif seller3 == "n":
                print("등록이 취소되었습니다.")
            else:
                print("잘못입력되었습니다.")
#####################################################################################################
#관리자 페이지#
#== == == == == == == == == == == == =
#[1] 로그인
#[2] 회원가입
#[3] 대시보드
#[4] 상품등록
#[5] 상품수정
#[6] 로그아웃
#[7] 뒤로가기
#[8] 프로그램종료

        elif seller in sellers:
            subrun2 = True
            subrun =True
            while subrun :
                print(menu)
                sel = input(">>>")
                if sel == "1":
                    print("=========================")
                    print("[로그인]\t아이디와 비밀번호를 입력")
                    id =input("아이디:")
                    if id in ids:
                        idx = ids.index(id)
                        pw = input("비밀번호 :")
                        if pw in pws[idx]:
                            print(f"로그인되었습니다.\n[{names[idx]}]님 환영합니다.")

                            login_user = idx
                        else:
                            print("잘못된 비밀번호입니다.")
                    else:
                        print("존재하지 않은 아이디입니다.")

                elif sel == "2":
                    print("=========================")
                    print("회원가입")
                    id = input("아이디 : ")
                    pw = input("비밀번호 : ")
                    name = input("이름 : ")
                    num = input("연락처 : ")
                    print("=========================")
                    print("입력하신 정보를 확인해주세요.\n저장하시겠습니까? (y/n)")
                    Sto =input(f"아이디 :{id}\n비밀번호 :{pw}\n이름 :{name}\n연락처 :{num}\n>>>")

                    if Sto == "y":
                        print("회원가입이 완료되었습니다.")
                        ids.append(id)
                        pws.append(pw)
                        names.append(name)
                        numbers.append(num)
                        sn = len(sns)+1
                        sns.append(sn)

                    elif Sto == "n":
                        print("회원가입이 취소되었습니다.")
                    else:
                        print("잘못입력되었습니다.")

                elif sel == "3":
                    if login_user is None :
                        print("로그인 후 이용해주세요.")
                        continue

                    print("=========================")
                    print("대시보드")
                    print("=========================")
                    total = 0
                    for j in range(len(product_no)):
                        total += (details_s[j] * selling_price[j])

                    print(f"▶▶총 매출 {total}원입니다.◀◀")
                    print("=========================")

                    for i in range(len(product_no)):
                        print(f"[상품번호 {product_no[i]}]\n상품명 :{product_menu[i]}|판매가격 :{selling_price[i]}원\n재고수량 :{inventory_quantity[i]}|판매상태 :{sales_status[i]} \n_________________________\n총 판매수량: {details_s[i]}|총 금액 :{details_s[i] * selling_price[i]}")
                        print("=========================\n")


                elif sel == "4":
                    if login_user is None :
                        print("로그인 후 이용해주세요.")
                        continue

                    print("=========================")
                    print("상품등록")
                    print("=========================")
                    pro_menu =input("상품명 : ")
                    price = int(input("판매가격 : "))
                    quantity = int(input("재고수량 : "))
                    sel=input(f"상품명 : {pro_menu}\n판매가격 :{price}원\n재고수량 :{quantity}개\n상품을 등록하시겠습니까? (y/n)\n>>>")

                    if sel == "y":
                        print("상품이 등록되었습니다.")
                        product_menu.append(pro_menu)
                        selling_price.append(price)
                        inventory_quantity.append(quantity)
                        details_s.append(0)
                        sn = len(product_no)+1
                        product_no.append(sn)
                        if quantity <= 0:
                            sales_status.append("품절")
                        elif quantity > 0:
                            sales_status.append("판매중")

                    elif sel == "n":
                        print("상품등록이 취소되었습니다.")
                    else:
                        print("잘못입력되었습니다.")



##################################################################################################
#상품수정페이지
#[1] 상품수정
#[2] 입출고관리
#[3] 상품품절
#[4] 상품삭제
#[5] 로그아웃
#[6] 뒤로가기
#[7] 프로그램종료
                elif sel == "5":
                    subrun2 = True
                    while subrun2 :

                        print(submenu) #상품수정페이지
                        sel1 = input(">>>")
                        if sel1 == "1": # 상품수정
                            print("=========================")
                            print("상품수정")

                            for i in range(len(product_no)):
                                print(f"상품번호{product_no[i]}. 상품명 :{product_menu[i]}")

                            sn = int(input("수정하실 상품번호를 입력해주세요\n>>>"))
                            if sn in product_no:
                                idx = product_no.index(sn)
                                print(f"수정하실 상품은 {product_menu[idx]}입니다.")
                                pro_menu = input("상품명 : ")
                                price = int(input("판매가격 : "))
                                quantity = int(input("재고수량 :"))
                                sel2= input(f"상품명 : {pro_menu}\n판매가격 :{price}원\n재고수량 :{quantity}개\n상품을 수정하시겠습니까? (y/n)\n>>>")
                                if sel2 == "y":
                                    print(f"""상품명 : {product_menu[idx]}▶▶▶{pro_menu}
판매가격 : {selling_price[idx]}▶▶▶{price}
재고수량 : {inventory_quantity[idx]}▶▶▶{quantity}로
수정되었습니다.""")
                                    product_menu[idx] = pro_menu
                                    selling_price[idx] = int(price)
                                    inventory_quantity[idx] = int(quantity)

                                    if inventory_quantity[idx] == 0 :
                                        sales_status[idx] = "품절"
                                    elif inventory_quantity[idx] > 0 :
                                        sales_status[idx] = "판매중"


                        elif sel1 == "2": # 입출고관리
                            print("=========================")
                            print("입출고관리")
                            for i in range(len(product_no)):
                                print(f"상품번호{product_no[i]}. 상품명 :{product_menu[i]}\t|현재 재고 : {inventory_quantity[i]}")

                            sn = int(input("입출고관리하실 상품번호를 입력해주세요\n>>>"))
                            if sn in product_no:
                                idx = product_no.index(sn)
                                quantity = int(input(f"{product_menu[idx]}상품의 현재 수량을 입력해주세요."))
                                sel2 = input("입력하신 수량으로 변경처리하겠습니까? (y/n)\n>>>")
                                if sel2 == "y":
                                    print(f"수정된 상품 : {product_menu[idx]}\n수량이 [{inventory_quantity[idx]}]▶▶▶[{quantity}]로 변경되었습니다. ")
                                    inventory_quantity[idx] = quantity
                                    if inventory_quantity[idx] == 0 :
                                        sales_status[idx] = "품절"
                                elif sel2 == "n":
                                    print("수정하신 내용이 취소되었습니다.")


                        elif sel1 == "3": # 판매상태변경
                            print("=========================")
                            print("판매상태변경")
                            for i in range(len(product_no)):
                                print(f"상품번호{product_no[i]}. 상품명 :{product_menu[i]}|판매상태 : {sales_status[i]}")
                            sn = int(input("판매상태변경하실 상품번호를 입력해주세요.\n>>>"))
                            if sn in product_no:
                                idx = product_no.index(sn)
                                status  = input(f"{product_menu[idx]}상품의 변경하실 판매상태를 선택해주세요.\n[1]판매중\n[2]품절\n[3]취소\n>>>")
                                if status == "1":
                                    print("=========================")
                                    print("판매중으로 변경처리되었습니다.")
                                    sales_status[idx] = "판매중"
                                elif status == "2":
                                    print("=========================")
                                    print("품절로 변경처리되었습니다.")
                                    sales_status[idx] = "품절"
                                elif status == "3":
                                    print("=========================")
                                    print("판매상태변경이 취소되었습니다.")


                        elif sel1 == "4": # 상품삭제
                            print("=========================")
                            print("상품삭제")
                            for i in range(len(product_no)):
                                print(f"상품번호{product_no[i]}. 상품명 :{product_menu[i]}|판매상태 : {sales_status[i]}")
                            sn = int(input("삭제하실 상품번호를 입력해주세요\n>>>"))

                            if sn in product_no:
                                idx = product_no.index(sn)
                                print(f"상품번호{product_no[idx]}. 상품명 :{product_menu[idx]}을")

                                sel2 = input("삭제하시겠습니까? (y/n)\n>>>")
                                if sel2 == "y":
                                    print("삭제처리되었습니다.")
                                    product_no.pop(idx)
                                    product_menu.pop(idx)
                                    selling_price.pop(idx)
                                    inventory_quantity.pop(idx)
                                    sales_status.pop(idx)
                                elif sel2 == "n":
                                    print("삭제처리가 취소되었습니다.")


                        elif sel1 == "5": # 로그아웃
                            print("=========================")
                            print("로그아웃되었습니다.")
                            login_user = None
                            subrun2 = False
                        elif sel1 == "6": # 뒤로가기
                            break
                        elif sel1 == "7":
                            subrun2 = False
                    else:
                        pass


##################################################################################################
                elif sel == "6": # 로그아웃
                    print("=========================")
                    print("로그아웃되었습니다.")
                    login_user = None
                    subrun = False
                elif sel == "7": # 뒤로가기
                    break

                elif sel == "8":
                    exit()




#####################################################################################################
    elif sel == "3":
        run = False
#####################################################################################################
    else:
        pass
#####################################################################################################
