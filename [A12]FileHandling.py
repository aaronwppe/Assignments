from datetime import date
from switch import Switch2


class Product:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_list(self):
        return [self.name, self.price, self.quantity]

    def __str__(self):
        return f'{self.code}\t{self.name}\t{self.price}\t{self.quantity}'


class Inventory:
    def __init__(self):
        self.product_dict = dict()

    def __iter__(self):
        self.product_dict_iter = iter(self.product_dict.items())
        return self

    def __next__(self):
        key, value = next(self.product_dict_iter)
        return Product(key, value[0], value[1], value[2])

    def add(self, product: Product):
        if product.code not in self.product_dict:
            self.product_dict[product.code] = product.to_list()

    @staticmethod
    def get_file_name(d=date.today()):
        return f'Product_{d.day}_{d.month}_{d.year}.txt'

    def to_csv(self):
        ret = str()
        for product in self:
            ret += f'{product.code},{product.name},{product.price},{product.quantity}\n'

        return ret

    def write_to_file(self):
        file_name = self.get_file_name()

        with open(file_name, 'a') as file:
            file.writelines(self.to_csv())

    @classmethod
    def read_from_file(cls):
        self = cls()
        file_name = self.get_file_name()
        
        with open(file_name, 'r') as file:
            for line in file:
                line_list = line.split(',')

                # invalid sequence
                if len(line_list) != 4:
                    continue

                # price and quantity is not of type 'int'
                if not (line_list[2].isnumeric() or line_list[3].isnumeric()):
                    continue

                product = Product(line_list[0], line_list[1], int(line_list[2]), int(line_list[3]))
                self.add(product)

        return self


def insert():
    inventory = Inventory()
    flag = 'y'
    while flag == 'y':
        try:
            print('Product,')
            code = int(input('Code: '))
            name = input('Name: ')
            price = int(input('Price: '))
            quantity = int(input('Quantity: '))
            inventory.add(Product(code, name, price, quantity))
            print('Product inserted!')
        except ValueError:
            print("ERROR: Value provided must be of type 'int'! Try again...")

        while 1:
            flag = input('Continue Insertion (y/n) ? ')
            if flag != 'y' and flag != 'n':
                print('Invalid input! Try Again...')
            else:
                break

    inventory.write_to_file()
    return 'Exited insertion mode.'


def read():
    ret = str()

    try:
        inventory = Inventory().read_from_file()
        for product in inventory:
            ret += str(product) + '\n'
    except FileNotFoundError:
        pass

    if ret == '':
        ret = 'No product data available!'

    return ret


switch = Switch2()
switch.add_case('Insert', insert)
switch.add_case('Read', read)
switch.add_exit_case()

print("Options:")
print(switch.options)

while not switch.exit_is_selected:
    option = input("Perform: ")
    print(switch.run(option))
    print(switch.break_line)
