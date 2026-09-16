# Классы и инварианты объектов
class Stock:
    def __init__(self, quantity):
        if type(quantity) is not int or quantity < 0:
            raise ValueError("неверный остаток")
        self.quantity = quantity
    def take(self, count):
        if type(count) is not int or not 0 <= count <= self.quantity:
            raise ValueError("нельзя выдать")
        self.quantity -= count

s = Stock(5)
s.take(2)
assert s.quantity == 3
