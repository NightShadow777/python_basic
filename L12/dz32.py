class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
       product =""
       for p_item in self.products.items():
        	n, p = p_item
        	product += str(n.name)+ ": " + str(p) + "pcs.\n"
       cart_decor = "###"*3
       cart_decor_1 = "---" * 2
       return f"\n{cart_decor} CART {cart_decor}\n" \
              f"User: {self.user}\n" \
              f"{cart_decor_1} Items: {cart_decor_1}" \
              f"\n{product}"

    def get_total(self):
        for key, cnt in self.products.items():
            self.total += key.price * cnt
        return self.total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
blackberry = Item('blackberry', 20, "blackberry", "middle", )
#print(lemon)  # lemon, price: 5
#print(blackberry)

buyer = User("Ivan", "Ivanov", "02628162")
buyer2 = User("Jon", "Doill", "255952292")
#print(buyer)  # Ivan Ivanov
#print(buyer2)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(str(cart) + "####"*6)
print("Total: ", end=" ")
print(cart.get_total()) # 60
print("####"*6)

cart2 = Purchase(buyer2)
cart2.add_item(blackberry, 4)
print(str(cart2) + "####"*6)
print("Total: ", end=" ")
print(cart2.get_total()) # 60
print("####"*6)