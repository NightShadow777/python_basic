'''
Создать класс цифрового счетчика. В классе реализовать методы:

    установка максимального значения счетчика,
    установка минимального значения счетчика
    установка начального значения счётчика
    метод увеличения счетчика на 1. Метод можно вызывать до тех пор, пока значение не достигнет максимума.
    Потом - выкинуть (raise) исключение ValueError, с описанием, что достигнут максимум
    уменьшения счетчика на 1. Метод можно вызывать до тех пор, пока значение не достигнет минимума. Потом -
    выкинуть (raise) исключение ValueError, с описанием, что достигнут минимум
    возвращения текущего значения счётчика

Начальное, минимальное и максимальное значения счетчика, также могут быть добавлены в метод инициализации экземпляра класса.


Приблизительный каркас для класса и варианты проверки. Вам нужно дописать необходимое вместо pass
'''
class Counter():
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start


    def set_max(self, max_max):
        pass

    def set_min(self, min_min):
        pass

    def step_up(self):
        pass

    def step_down(self):
        pass

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(counter.get_current())  # 10
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
print(counter.get_current())  # 10
