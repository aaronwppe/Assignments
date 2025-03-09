class InvalidProductCode(Exception):
    message = 'Product code provided does not exist!'


class NegativeProductQuantity(Exception):
    message = 'Quantity cannot be negative!'


class MaxProductQuantityExceeded(Exception):
    message = 'Maximum product quantity exceeded!'


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


flag = 'y'
while flag == 'y':
    try:
        p = Product(input("Code: "), int(input("Quantity: ")))
        print('Product is valid.')
    except (InvalidProductCode, NegativeProductQuantity, MaxProductQuantityExceeded) as e:
        print(f'ERROR: {e.message}')
    except ValueError:
        print(f"ERROR: Quantity value provided must be of type 'int'!")

    while 1:
        flag = input('Continue Insertion (y/n) ? ')
        if flag != 'y' and flag != 'n':
            print('Invalid input! Try Again...')
        else:
            break


print("Bye!")
