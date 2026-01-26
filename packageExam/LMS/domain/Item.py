class Item:
    CATEGORY_ETC = "잡화"
    CATEGORY_DRINK = "음료"
    CATEGORY_IT = "IT"
    CATEGORY_BOOK ="도서"

    CATEGORIES = [
        CATEGORY_ETC,
        CATEGORY_DRINK,
        CATEGORY_IT,
        CATEGORY_BOOK]

    def __init__(self, name, description, price, stock,category,active=True):
        if category not in self.CATEGORIES:
            raise ValueError ("잘못된 카테고리입니다.")

        self.name = name                                # 상품명
        self.description = description                  # 상품 설명
        self.price = price                              # 가격
        self.stock = stock                              # 재고
        self.active = active                            # 판매중, 판매중지
        self.category = category                        # 카테고리

    def decrease_stock(self, qty=1):
        if self.stock < qty:
            return False
        self.stock -= qty
        return True

    def __str__(self):
        status = "판매중" if self.active else "판매중지"
        return f'{self.name}|{self.description}|{self.price}|{self.stock}|{status}'

    def to_line(self):
        return f'{self.name}|{self.description}|{self.price}|{self.stock}|{self.active}|{self.category}\n'

    @staticmethod
    def from_line(line:str):
        name, description, price, stock, category,active = line.strip().split("|")
        return Item(
            name=name,
            description=description,
            price=int(price),
            stock=int(stock),
            category=category,
            active=(active == "True"))
