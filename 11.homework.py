'''
Создайте пользовательский класс для описания товара (предположим, это задел для интернет-магазина).
В качетсве полей товара можете использовать цены, описание, габариты товара. Создайте пару экземпляров вашего класса и
протестируйте их работу.
'''
class Goods:
    def __init__(self, price, description, size):
        self.price = price
        self.description = description
        self.size = size
    def __str__(self):
        return "Your good[ name = {}, price = {}, size = {}]".format(self.description, self.price, self.size)

good_1 = Goods(50, "juice", "small")
good_2 = Goods(30, "water", "small")
good_3 = Goods(60, "milk", "small")

print(good_1)
print(good_2)
print(good_3)
'''
Создайте класс "Покупатель". В качестве полей можете испольщовать фамилию, имя, отчество, моб. телефон и т.д..
'''
class Buyer:
    def __init__(self, name, surname, number, email):
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email
    def __str__(self):
        return "Buyer[ ID = {} {}],\nСD = [{}, {}]".format(self.surname, self.number, self.number, self.email)
Buyer_1 = Buyer("Adrian", "Dirty-raincoat", "+3803437654", "potfolion@gmail.com")
print(Buyer_1)
'''
Создайте класс "Заказ". Заказ может содержать несколько товаров. Заказ должен содержать данные о пользователе,
который его осуществил. Реализуйте метод вычисления суммарной стоимости заказа. Определите метод __str__() для
корректного вывода информации о этом заказе.
'''
class Order:
    def __init__(self, name, surname, product):
        self.name = name
        self.surname = surname
        self.product = product

    def whole_price(self):
        full_price = 0
        for element in self.product.values():
            full_price += element
        return "Full price : {}".format(full_price)

    def __str__(self):
        return "Buyer[ ID = {} {}],\nProduct = [{}]".format(self.name, self.surname, self.product)

Buyer_1 = Order("Adrian", "Dirty-raincloak", {"Milk":50, "Water":15})

print(Buyer_1)
print(Buyer_1.whole_price())