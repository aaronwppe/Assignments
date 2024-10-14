class InvalidProductCode(Exception):
    pass


class NegativeProductQuantity(Exception):
    pass


class MaxProductQuantityExceeded(Exception):
    pass


class Product:
    max_quantity = {'A1': 5, 'A2': 3,
                    'B1': 10, 'B2': 19}

    def __init__(self, code, quantity):
        self.code = code
        self.quantity = quantity

        self.validate()

    def validate(self):
        if self.code not in Product.max_quantity:
            raise InvalidProductCode

        if self.quantity < 0:
            raise NegativeProductQuantity

        if self.quantity > Product.max_quantity[self.code]:
            raise MaxProductQuantityExceeded


try:
    p = Product(input("code: "), 5)
except InvalidProductCode:
    print('e1')
    exit(1)
except NegativeProductQuantity:
    print('e2')
    exit(1)
except MaxProductQuantityExceeded:
    print('e3')
    exit(1)

print(p)
