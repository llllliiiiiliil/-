class Coffeeshop:
    def __init__(self,name,property,menu):
        self.name = "박한"
        self.property = 1000000
        self.menu = {
            "iceamericano": 1000,
            "latte": 1000,
            "soda": 1000
        }

    def addmenu(self):
        menu = input("메뉴 이름을 입력해 주세요:")
        price = input("가격을 입력해 주세요")
        self.menu[menu] = price
    def intro(self):
        print(f"가게 이름은 {self.name}이고 재산은 {self.property}입니다")

    def showmenu(self):
        for x,y in self.menu.items():
            print(f"이름은{x} 가격은 {y}입니다")
