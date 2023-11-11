
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other_bank):
        self._balance += other_bank._balance


class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            print("Ошибка: деление на ноль.")
            return None






my_bank = Bank("My Bank", 100)
your_bank = Bank("Your Bank", 100)

my_bank._merge_balance(your_bank)
print(f"My balance: {my_bank._balance}, Your balance: {your_bank._balance}")


calc1 = Calculator(10)
calc2 = Calculator(5)

result_add = calc1 + calc2
result_sub = calc1 - calc2
result_mul = calc1 * calc2
result_div = calc1 / calc2

print(f"Addition: {result_add}, Subtraction: {result_sub}, Multiplication: {result_mul}, Division: {result_div}")


