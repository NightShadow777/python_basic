'''
1) Создайте пользовательский класс для описания товара (предположим, это задел для интернет-магазина). 
В качестве полей товара можете использовать значение цены, описание,

габариты товара. Создайте пару экземпляров вашего класса и протестируйте их работу.

2) Создайте класс «Покупатель». В качестве полей можете использовать фамилию, имя, отчество, мобильный телефон и т. д.

3) Создайте класс «Заказ». Заказ может содержать несколько товаров, причем количество каждого из товаров может быть разными.
 Заказ должен быть "подвязан" к пользователю, который его осуществил. Реализуйте метод вычисления суммарной стоимости заказа. 
 Определите метод __str__() для корректного вывода информации о этом заказе.


Код можно начать вот так:
'''

class Item:
    def __init__(self, name, price, decription, demensions):
        self.price = price
        self.decription = decription
        self.demensions = demensions
        self.name = name

    def __str__(self):
        return f"name = {self.name}, desc = {self.decription}, demensions = {self.demensions}, price = {self.price}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        pass


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        pass

    def get_total(self):
        pass

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

'''
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
'''

print(cart.get_total())  # 60