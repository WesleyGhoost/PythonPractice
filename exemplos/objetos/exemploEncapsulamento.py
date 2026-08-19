class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def __validate(self, amount):
        if amount < 0:
            raise ValueError("O valor deve ser negativo")
        return

    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError("Fundos insuficientes")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

operation_one = Wallet(50)
operation_one.deposit(100)
operation_one.withdraw(50)
print(operation_one.get_balance())

operation_two = Wallet(-10)
operation_two.deposit(60)
operation_two.withdraw(-20)
print(operation_two.get_balance())