from switch import *


class Account:
    bank_name = "My Bank"
    currency = "Rs"
    counter = 0
    min_bal = 3000

    def __init__(self, name, acc_type):
        Account.counter += 1
        self.number = Account.counter
        self.name = name
        self.type = acc_type
        self.balance = 0

    @classmethod
    def create(cls, name, acc_type, opening_bal):
        if opening_bal < cls.min_bal:
            return f'Opening Balance must be at least {cls.min_bal}!'

        acc = cls(name, acc_type)
        acc.deposit(opening_bal)
        return acc

    def deposit(self, amount):
        if amount <= 0:
            return 'Invalid amount! Amount must be greater than 0.'

        self.balance += amount
        return 'Deposit successful!'

    def withdraw(self, amount):
        new_bal = self.balance - amount

        if new_bal < Account.min_bal:
            return f'Must maintain minimum balance of {Account.min_bal}.'

        self.balance = new_bal
        return 'Withdrawal successful!'

    @property
    def details(self):
        return (f'Bank Name: {Account.bank_name}\n' +
                f'Account Number: {self.number}\n' +
                f'Holder Name: {self.name}\n' +
                f'Account Type: {self.type}\n' +
                f'Balance: {self.balance} ' + Account.currency)


def input_int(prompt: str, default="Input must be a number! Please try again."):
    n = input(prompt)

    if n.isnumeric():
        return int(n)
    else:
        print(default)
        return input_int(prompt)


print("Account")
holder_name = input("Holder Name: ")
a_type = input("Account Type: ")
open_bal = input_int('Opening Balance: ')

while 1:
    account = Account.create(holder_name, a_type, open_bal)
    if type(account) is Account:
        break

    print('ERROR: ', account, 'Please try again.')
    open_bal = input_int('Opening Balance: ')
    continue

switch = Switch()
switch.add_case("Display Details", lambda: print(account.details))
switch.add_case("Deposit", lambda: print(account.deposit(input_int("Deposit amount: "))))
switch.add_case("Withdraw", lambda: print(account.withdraw(input_int("Withdraw Amount: "))))

print(switch.break_line)
switch.run()